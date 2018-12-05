import passwordmeter
from src.services.main import *

data_service = DataService()
password_checker = passwordmeter.Meter(settings=dict(factors='length,charmix'))


def check_registration_input(user_name, password, re_entered_password):
    errors = []
    user_name_exists = data_service.check_if_user_name_exists(user_name)
    strength, improvements = password_checker.test(password)
    if len(user_name) < 5:
        errors.append(str(len(errors) + 1) + '. User Name must contain atleast 5 characters.')
    if user_name_exists:
        errors.append(str(len(errors) + 1) + '. User Name already exists.')
    if strength < 0.7:
        errors.append(str(len(errors) + 1) + '. Password too weak. Try a strong password.')
    if password != re_entered_password:
        errors.append(str(len(errors) + 1) + '. Password and Re-entered password do not match.')
    return errors

