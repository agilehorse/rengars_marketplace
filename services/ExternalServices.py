import atexit
import sys

import pika
from flask import json
from py_eureka_client import eureka_client

from env_vars import EUREKA_EXCHANGE, EUREKA_URL, MARKETPLACE_PORT, RABBIT_URL
from models.QueueMessage import QueueMessage
from models.QueueMessageType import QueueMessageType
from models.RestException import RestException
from models.User import User

if EUREKA_URL:
    eureka_client.init(eureka_server=EUREKA_URL,
                       app_name="marketplace-service",
                       instance_port=MARKETPLACE_PORT)

message_queue_connection = None
if RABBIT_URL is not None:
    message_queue_connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL))
    message_queue = message_queue_connection.channel()


class ExternalServices:
    @staticmethod
    def call_eureka(user_id):
        if not EUREKA_URL:
            return User(user_id)
        response = eureka_client.do_service("user-service", "/users/" + user_id, return_type='response_object')
        status = response.status
        body = json.loads(response.read().decode('utf-8'))
        if status != 200:
            raise RestException("errors.users.non_ok", status, body)
        return body

    @staticmethod
    def get_user_info(user_id):
        try:
            body = ExternalServices.call_eureka(user_id)
        except Exception as e:
            print(e)
            raise RestException("errors.users.service_off", 503)

        contact = body.get('contact', {})
        email = contact.get('email')
        birth_date = body.get('birthDate')
        phone_number = contact.get('phoneNumber')
        return User(user_id, email, birth_date, phone_number)

    @staticmethod
    def publish_to_message_queue(event_type: QueueMessageType, body: dict):
        """Publishes message to message queue.
        """
        queue_message = QueueMessage(body['id'], event_type, body)
        try:
            message_queue.basic_publish(exchange=EUREKA_EXCHANGE,
                                        body=queue_message)
        except Exception as e:
            print(e)


def cleanup_application():
    print("closing")
    if message_queue_connection is not None:
        message_queue_connection.close()
    sys.exit()


atexit.register(cleanup_application)
