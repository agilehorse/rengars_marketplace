import os

import connexion
from flask_pymongo import PyMongo

application = connexion.App(__name__, specification_dir='swagger/')
flask_app = application.app
flask_app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ[
    'MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
db = PyMongo(flask_app).db
application.add_api('swagger.yaml', arguments={'title': 'Rengars Marketplace API'})
