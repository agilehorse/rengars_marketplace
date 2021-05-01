import logging

from flask_testing import TestCase

from App import flask_app


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        return flask_app
