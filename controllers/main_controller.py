import connexion

from env_vars import EUREKA_URL
from services.ExternalServices import ExternalServices


def hello():
    return "Hello", 200


def eureka():
    if not EUREKA_URL:
        return connexion.problem(500, "Internal Server error", "Eureka url not set", "errors.eureka")
    if not ExternalServices.eureka_on:
        ExternalServices.init_eureka()
        if not ExternalServices.eureka_on:
            return connexion.problem(500, "Internal Server error",
                                     "Unable to connect to eureka, the server might not be running", "errors.eureka")

        return "OK", 200
