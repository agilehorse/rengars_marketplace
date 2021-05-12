from datetime import datetime

from models.User import User


def get_user_info(user_id):
    # todo finish eureka
    # user = eureka_client.do_service("user-service", "/service/context/path")
    user = User(user_id, "tests@email.com", datetime.now(), '+420 123 456 789')
    return user
