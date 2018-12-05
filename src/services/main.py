from src.models import *
import bcrypt


class DataService:
    user = None
    user_credential = None

    def __init__(self):
        self.user = UserDetail
        self.user_credential = UserCredential

    def get_user_by_email(self, email):
        users = self.user.objects(email=email)
        return users[0] if len(users) > 0 else None

    def get_user_by_user_name(self, user_name):
        user_credentials = self.user_credential.objects(user_name= user_name)
        return user_credentials[0] if len(user_credentials) > 0 else None

    def get_user_by_user_id(self, user_id):
        user_credentials = self.user_credential.objects(user=user_id)
        return user_credentials[0] if len(user_credentials) > 0 else None

    @staticmethod
    def create_user_credential(user_name, password):
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        new_user_credential = UserCredential(user_name=user_name, password=hashed_password)
        new_user_credential.save()
        print "created ..."
        return new_user_credential if new_user_credential.id else None

    def check_if_user_name_exists(self, user_name):
        user_credentials = self.user_credential.objects(user_name=user_name)
        return True if len(user_credentials) > 0 else False

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