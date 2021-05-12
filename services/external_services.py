from flask import json
from py_eureka_client import eureka_client

from models.RestException import RestException
from models.User import User


def get_user_info(user_id):
    try:
        response = eureka_client.do_service("user-service", "/service/context/path", return_type='response_object')
        status = response.status
        body = json.loads(response.read().decode('utf-8'))
        if status != 200:
            raise RestException("errors.users.non_ok", status, body)
        contact = body.get('contact', {})
        email = contact.get('email')
        birth_date = body.get('birthDate')
        phone_number = contact.get('phoneNumber')
        return User(user_id, email, birth_date, phone_number)
    except:
        raise RestException("errors.users.service_off", 503)
