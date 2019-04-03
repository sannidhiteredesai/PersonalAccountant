from tinydb import Query
from pa import get_db
from pa.config import Config


class BankDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('banks')

    def add(self, new_bank):
        # new_bank.update({'username': for_user})
        # self.db.insert(new_bank)
        pass

    def get_all_banks(self, for_user):
        pass

