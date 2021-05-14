from os import environ

APP_ENV = environ.get("APP_ENV")
EUREKA_URL = environ.get('EUREKA_URL')
print(f"==============================={EUREKA_URL}----------------")
EUREKA_EXCHANGE = environ.get('EUREKA_EXCHANGE')
RABBIT_URL = environ.get("RABBIT_URL")
MARKETPLACE_PORT = environ.get("MARKETPLACE_PORT", 5000)
