from tinydb import Query
from pa import get_db
from pa.config import Config


class BankDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('banks')

    def add(self, new_bank):
        self.db.insert(new_bank)

    def get_all_banks(self, for_user):
        return self.db.search(Query().username == for_user)
