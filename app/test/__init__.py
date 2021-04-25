import logging

import connexion
from flask_testing import TestCase
from utils.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app
