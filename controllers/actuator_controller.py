from flask import request

from services.ExternalServices import message_queue_connection


def get_actuators():
    url = request.url
    return {"_links": {"self": {"href": url, "templated": False},
                       "health": {"href": url + "/health", "templated": False},
                       "info": {"href": url + "/info", "templated": False},
                       "shutDown": {"href": url + "/shutDown", "templated": False}
                       }
            }


def get_health():
    return {"status": "UP"}, 200


def get_info():
    return {}, 200


def shut_down():
    if message_queue_connection is not None:
        message_queue_connection.close()
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return {}, 200
