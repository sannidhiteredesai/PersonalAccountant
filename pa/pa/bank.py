from pa.config import Config
from pa.db.bank import BankDB


class Banks:
    def __init__(self, config=Config):
        self.banks = BankDB(config)

    def add(self, new_bank, for_user):
        new_bank.update({'username': for_user})
        self.banks.add(new_bank)

    def get_all_banks(self, for_user):
        banks = self.banks.get_all_banks(for_user=for_user)
        return_banks = []
        for bank in banks:
            return_banks.append({
                'bank_name': bank['bank_name'],
                'bank_branch': bank['bank_branch'],
                'branch_address': bank['branch_address'],
                'timings': bank['timings'],
            })
        return return_banks

    def get_all_bank_branch_names(self, for_user):
        banks = self.banks.get_all_banks(for_user=for_user)
        bank_branches = {}
        for bank in banks:
            if bank['bank_name'] in bank_branches:
                bank_branches[bank['bank_name']].append(bank['bank_branch'])
            else:
                bank_branches[bank['bank_name']] = [bank['bank_branch']]
        return bank_branches

    def get_all_branches_of_a_bank(self, bank_name, for_user):
        banks = self.banks.get_all_banks(for_user=for_user)
        return sorted([bank['bank_branch'] for bank in banks if bank['bank_name'] == bank_name])

    def delete_bank_branch(self, bank_name, bank_branch, username):
        self.banks.delete_bank_branch(bank_name=bank_name, bank_branch=bank_branch, username=username)
