from pa.config import Config
from pa.db.bank import BankDB


class Banks:
    def __init__(self, config=Config):
        self.banks = BankDB(config)

    def add(self, new_bank, for_user):
        self.banks.add(new_bank, for_user)