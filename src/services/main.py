from src.models import *
import bcrypt


class DataService:
    user = None
    user_credential = None

    def __init__(self):
        self.user = User
        self.user_credential = UserCredential

    def get_user_by_email(self, email):
        users = self.user.objects(email=email)
        return users[0] if len(users) > 0 else None

    def get_user_credential_by_user_id(self, user_id):
        user_credentials = self.user_credential.objects(user=user_id)
        return user_credentials[0] if len(user_credentials) > 0 else None

    def check_credentials(self, entered_email, entered_password):
        desired_user = self.get_user_by_email(entered_email)
        if desired_user is None:
            return False
        desired_user_credential = self.get_user_credential_by_user_id(desired_user.id)
        if bcrypt.checkpw(entered_password.encode('utf8'), desired_user_credential.password.encode('utf8')):
            return True
        else:
            return False

    # def create_user(self, e, f, l, p):
    #     u = User(email=e, first_name=f, last_name=l)
    #     u.save()
    #     p = bcrypt.hashpw(p, bcrypt.gensalt(14))
    #     uc = UserCredential(user=u, password=p)
    #     uc.save()


# if __name__ == "__main__":
#     d = DataService()
#     d.create_user('adharshrp@gmail.com', 'Adharsh', 'Rajan', 'abc123')
#     print d.check_credentials('adharshrp@gmail.com', "abc123")