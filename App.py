from os import environ

import connexion
from flask_pymongo import PyMongo
from mongomock.mongo_client import MongoClient as PyMongoMock

application = connexion.App(__name__, specification_dir='swagger/')
flask_app = application.app
if environ.get("test") == "true":
    flask_app.config['TESTING'] = True
    application.db = PyMongoMock().db
else:
    flask_app.config["MONGO_URI"] = 'mongodb://' + environ['MONGODB_USERNAME'] + ':' + environ[
        'MONGODB_PASSWORD'] + '@' + environ['MONGODB_HOSTNAME'] + ':27017/' + environ['MONGODB_DATABASE']
    application.db = PyMongo(flask_app).db

application.add_api('swagger.yaml', arguments={'title': 'Rengars Marketplace API'})
