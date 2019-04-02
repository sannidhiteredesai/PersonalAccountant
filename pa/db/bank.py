from tinydb import Query
from pa import get_db
from pa.config import Config


class BankDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('banks')

    def add(self, new_bank, for_user):
        # new_bank.update({'username': for_user})
        # self.db.insert(new_bank)
        pass

    def exists(self, member, for_user):
        # members = self.db.search((Query().membername == member) & (Query().username == for_user))
        # return True if members else False
        pass

    def get_members(self, for_user):
        # users = self.db.search(Query().username == for_user)
        # return users
        pass
