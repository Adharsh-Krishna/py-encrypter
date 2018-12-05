from src.services.main import *
import bcrypt

data_service = DataService()


def check_credentials(user_name, entered_password):
    desired_user = data_service.get_user_by_user_name(user_name)
    if desired_user is None:
        return False
    if bcrypt.checkpw(entered_password.encode('utf8'), desired_user.password.encode('utf8')):
        return True
    else:
        return False
