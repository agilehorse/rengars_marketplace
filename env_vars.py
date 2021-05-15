from os import environ

APP_ENV = environ.get("APP_ENV")
EUREKA_URL = environ.get('EUREKA_URL')
RABBIT_EXCHANGE = environ.get('RABBIT_EXCHANGE')
RABBIT_URL = environ.get("RABBIT_URL")
MARKETPLACE_PORT = int(environ.get("MARKETPLACE_PORT", 5000))
