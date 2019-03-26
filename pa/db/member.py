from tinydb import Query
from pa import get_db
from pa.config import Config


class MemberDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('members')

    def add(self, member, for_user):
        self.db.insert({'membername': member, 'username': for_user})

    def exists(self, member, for_user):
        members = self.db.search((Query().membername == member) & (Query().username == for_user))
        return True if members else False

    def get_members(self, for_user):
        users = self.db.search(Query().username == for_user)
        return users
