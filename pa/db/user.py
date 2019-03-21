from pa import get_db
from pa.config import Config
from tinydb import Query
from werkzeug.security import generate_password_hash, check_password_hash


class UserDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('users')

    def add(self, user):
        self.db.insert({
            'username': user.username,
            'password': generate_password_hash(user.password),
            'mobile': user.mobile,
            'dob': user.dob,
            'secret_question': user.secret_question,
            'answer': user.answer,
        })

    def exists(self, username):
        return bool(self.get_user(username))

    def exists_mobile(self, mobile):
        users = self.db.search(Query().mobile == mobile)
        return True if users else False

    def check_credentials(self, username, password):
        if self.exists(username):
            password_hash = self.get_user(username).get('password')
            return check_password_hash(password_hash, password)
        return False

    def get_user(self, username):
        users = self.db.search(Query().username == username)
        return users[0] if users else None

