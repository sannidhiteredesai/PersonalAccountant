from pa.db.user import UserDB
from pa.config import Config

class User:
    def __init__(self, details):
        self.username = details.get('username')
        self.password = details.get('password')
        self.mobile = int(details.get('mobile'))
        self.dob = details.get('dob').strftime("%d/%m/%Y")
        self.secret_question = details.get('question')
        self.answer = details.get('answer')

class Users:
    def __init__(self, config=Config):
        self.users = UserDB(config)

    def add(self, user):
        return self.users.add(user)

    def exists(self, username):
        return self.users.exists(username)

    def exists_mobile(self, mobile):
        return self.users.exists_mobile(mobile)

    def are_valid_credentials(self, username, password):
        return self.users.check_credentials(username=username, password=password)

    def get_user(self, username):
        return self.users.get_user(username=username)
