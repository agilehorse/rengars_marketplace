import pika
import requests
from flask import json
from py_eureka_client import eureka_client

from env_vars import RABBIT_EXCHANGE, EUREKA_URL, MARKETPLACE_PORT, RABBIT_URL
from models.QueueMessage import QueueMessage
from models.QueueMessageType import QueueMessageType
from models.RestException import RestException
from models.User import User


class ExternalServices:
    message_queue_connection = None
    message_queue = None
    eureka_on = False

    @staticmethod
    def create():
        ExternalServices.init_eureka()
        ExternalServices.init_rabbit()

    @staticmethod
    def init_eureka():
        if EUREKA_URL:
            try:
                eureka_client.init(eureka_server=EUREKA_URL,
                                   app_name="marketplace-service",
                                   instance_host="localhost",
                                   instance_port=MARKETPLACE_PORT,
                                   status_page_url="/actuator/info",
                                   health_check_url="/actuator/health",
                                   home_page_url="/ui")
                ExternalServices.eureka_on = True
            except Exception as e:
                print(e)
                ExternalServices.eureka_on = False

    @staticmethod
    def init_rabbit():
        if RABBIT_URL is not None and len(RABBIT_URL) > 1:
            url_params = RABBIT_URL.split(":")
            connection_params = pika.ConnectionParameters(host=url_params[0], port=url_params[1])
            try:
                ExternalServices.message_queue_connection = pika.BlockingConnection(connection_params)
            except Exception as e:
                print(e)
                ExternalServices.message_queue_connection = None
                return

            ExternalServices.message_queue = ExternalServices.message_queue_connection.channel()
            ExternalServices.message_queue.exchange_declare(exchange=RABBIT_EXCHANGE, durable=True, exchange_type='fanout')

    @staticmethod
    def call_eureka(user_id):
        if not EUREKA_URL:
            return {'id': user_id}
        if not ExternalServices.eureka_on:
            ExternalServices.init_eureka()
            if not ExternalServices.eureka_on:
                raise Exception()

        instances = eureka_client.get_client().applications.get_application("USER-SERVICE").up_instances
        if len(instances) > 0:
            instance = instances[0]
            url = f"http://{instance.hostName}:{instance.port.port}/users/{user_id}"
            response = requests.get(url)
            status = response.status_code
            body = json.loads(response.text)
            if status != 200:
                raise RestException("errors.users.non_ok", status, body)
            return body
        raise RestException("errors.users.non_ok", 503)

    @staticmethod
    def get_user_info(user_id):
        try:
            body = ExternalServices.call_eureka(user_id)
        except RestException as re:
            print(re)
            raise re
        except Exception as e:
            print(e)
            raise RestException("errors.users.service_off", 503)

        contact = body.get('contactDTO', {})
        email = contact.get('email')
        birth_date = body.get('birthDate')
        phone_number = contact.get('phoneNumber')
        return User(user_id, email, birth_date, phone_number)

    @staticmethod
    def publish_to_message_queue(event_type: QueueMessageType, body: dict):
        """Publishes message to message queue.
        """
        if ExternalServices.message_queue_connection is None:
            ExternalServices.init_rabbit()
            if ExternalServices.message_queue_connection is None:
                return

        queue_message = QueueMessage(body['id'], event_type, body)
        try:
            if ExternalServices.message_queue:
                ExternalServices.message_queue.basic_publish(exchange=RABBIT_EXCHANGE,
                                                             body=queue_message.toJSON(),
                                                             routing_key='')
        except Exception as e:
            print(e)

    @staticmethod
    def cleanup():
        if ExternalServices.message_queue_connection is not None:
            ExternalServices.message_queue_connection.close()
