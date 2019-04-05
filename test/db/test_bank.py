from unittest import TestCase
from pa.db.bank import BankDB


class TestConfig:
    DB = 'memory'


class TestBankDB(TestCase):

    def setUp(self):
        self.banks = BankDB(config=TestConfig)

    def test_add_and_get_all_banks_for_user(self):
        self.banks.add({'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'a', 'timings': '', 'username': 'u1'})
        self.banks.add({'bank_name': 'b2', 'bank_branch': 'br3', 'branch_address': 'a', 'timings': '', 'username': 'u2'})
        self.banks.add({'bank_name': 'b1', 'bank_branch': 'br2', 'branch_address': 'a', 'timings': '', 'username': 'u1'})

        self.assertEqual([
            {'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'a', 'timings': '', 'username': 'u1'},
            {'bank_name': 'b1', 'bank_branch': 'br2', 'branch_address': 'a', 'timings': '', 'username': 'u1'}
        ],self.banks.get_all_banks(for_user='u1'))

        self.assertEqual([
            {'bank_name': 'b2', 'bank_branch': 'br3', 'branch_address': 'a', 'timings': '', 'username': 'u2'}
        ], self.banks.get_all_banks(for_user='u2'))

        self.assertEqual([], self.banks.get_all_banks(for_user='u3'))

    def test_delete_bank_branch(self):
        self.banks.add({'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'a', 'timings': '', 'username': 'u1'})
        self.banks.add({'bank_name': 'b1', 'bank_branch': 'br2', 'branch_address': 'a', 'timings': '', 'username': 'u1'})
        self.banks.delete_bank_branch(bank_name='b1', bank_branch='br1', username='u1')
        self.assertEqual(
            [{'bank_name': 'b1', 'bank_branch': 'br2', 'branch_address': 'a', 'timings': '', 'username': 'u1'}
        ], self.banks.get_all_banks(for_user='u1'))
