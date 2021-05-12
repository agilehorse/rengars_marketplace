from os import environ

import connexion
import py_eureka_client.eureka_client as eureka_client
from flask_pymongo import PyMongo
from mongomock.mongo_client import MongoClient as PyMongoMock

APP_PORT = environ.get("APP_PORT", 5000)

application = connexion.App(__name__, specification_dir='swagger/')
flask_app = application.app
if environ.get("APP_ENV") == "test":
    flask_app.config['TESTING'] = True
    application.db = PyMongoMock().db
else:
    if (eureka_url := environ.get('EUREKA_URL')) is not None:
        eureka_client.init(eureka_server=eureka_url,
                           app_name="marketplace-service",
                           instance_port=APP_PORT)

    flask_app.config["MONGO_URI"] = 'mongodb://' + environ['MONGODB_USERNAME'] + ':' + environ[
        'MONGODB_PASSWORD'] + '@' + environ['MONGODB_HOSTNAME'] + ':27017/' + environ['MONGODB_DATABASE']
    application.db = PyMongo(flask_app).db

application.add_api('swagger.yaml', arguments={'title': 'Rengars Marketplace API'})
