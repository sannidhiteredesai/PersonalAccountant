from pa.pa.user import Users
from pa.ui import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(username):
    return LoginUser(Users().get_user(username=username).get('username'))


class LoginUser(UserMixin):
    def __init__(self, username): self.username = username
    def is_active(self): True
    def is_anonymous(self): False
    def is_authenticated(self): True
    def get_id(self): return self.username
