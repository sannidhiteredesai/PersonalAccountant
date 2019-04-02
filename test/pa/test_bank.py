from unittest import TestCase
from unittest.mock import patch

from pa.pa.bank import Banks


class TestConfig:
    DB = 'memory'


class TestBank(TestCase):

    @patch('pa.db.bank.BankDB.add')
    def test_add_bank(self, mock_add):
        banks = Banks(TestConfig)
        new_bank = {
            'bank_name': 'aa',
            'bank_branch': 'aa',
            'branch_address': 'a\r\nb\r\nc\r\n',
            'timings': '',
        }
        banks.add(new_bank, for_user='u1')
        mock_add.assert_called_with(new_bank, 'u1')

    def test_get_all_banks(self): pass

    def test_get_all_bank_branch_names(self): pass

    def test_get_all_branches_of_a_bank(self): pass
