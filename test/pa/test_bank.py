from unittest import TestCase
from unittest.mock import patch

from pa.pa.bank import Banks


class TestConfig:
    DB = 'memory'


class TestBank(TestCase):

    @patch('pa.db.bank.BankDB.add')
    def test_add_bank(self, mock_add):
        banks = Banks(TestConfig)
        banks.add({
            'bank_name': 'aa',
            'bank_branch': 'aa',
            'branch_address': 'a\r\nb\r\nc\r\n',
            'timings': '',
        }, for_user='u1')

        mock_add.assert_called_with({
            'bank_name': 'aa',
            'bank_branch': 'aa',
            'branch_address': 'a\r\nb\r\nc\r\n',
            'timings': '',
            'username': 'u1',
        })

    @patch('pa.db.bank.BankDB.get_all_banks')
    def test_get_all_banks(self, mock_get_all_banks):

        mock_get_all_banks.return_value = [
            {'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
            {'bank_name': 'b2', 'bank_branch': 'br2', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
            {'bank_name': 'b3', 'bank_branch': 'br3', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
        ]
        expected_all_banks = [
            {'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'aa', 'timings': ''},
            {'bank_name': 'b2', 'bank_branch': 'br2', 'branch_address': 'aa', 'timings': ''},
            {'bank_name': 'b3', 'bank_branch': 'br3', 'branch_address': 'aa', 'timings': ''},
        ]

        banks = Banks(TestConfig)
        all_banks = banks.get_all_banks(for_user='u1')
        self.assertEqual(expected_all_banks, all_banks)

    @patch('pa.db.bank.BankDB.get_all_banks')
    def test_get_all_bank_branch_names(self, mock_get_all_banks):

        mock_get_all_banks.return_value = [
            {'bank_name': 'b1', 'bank_branch': 'br1', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
            {'bank_name': 'b1', 'bank_branch': 'br2', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
            {'bank_name': 'b2', 'bank_branch': 'br3', 'branch_address': 'aa', 'timings': '', 'username': 'u1'},
        ]
        expected_all_bank_branch_names = [
            {'bank_name': 'b1', 'bank_branch': 'br1'},
            {'bank_name': 'b1', 'bank_branch': 'br2'},
            {'bank_name': 'b2', 'bank_branch': 'br3'},
        ]

        banks = Banks(TestConfig)
        all_bank_branch_names = banks.get_all_bank_branch_names(for_user='u1')
        self.assertEqual(expected_all_bank_branch_names, all_bank_branch_names)

    def test_get_all_branches_of_a_bank(self): pass
