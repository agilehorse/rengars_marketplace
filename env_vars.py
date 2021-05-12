from os import environ

APP_ENV = environ.get("APP_ENV")
EUREKA_URL = environ.get('EUREKA_URL')
EUREKA_EXCHANGE = environ.get('EUREKA_EXCHANGE')
RABBIT_URL = environ.get("RABBIT_URL")
APP_PORT = environ.get("APP_PORT", 5000)
