import datetime
from unittest import TestCase
from unittest.mock import patch

from pa.pa.fd import FDs


class TestConfig:
    DB = 'memory'


class TestBank(TestCase):

    def test_date_to_str(self):
        self.assertEqual('20190101', FDs.date_to_str(datetime.datetime(2019, 1, 1)))
        self.assertEqual('20190102', FDs.date_to_str(datetime.datetime(2019, 1, 2)))
        self.assertEqual('20190131', FDs.date_to_str(datetime.datetime(2019, 1, 31)))

    @patch('pa.db.fd.FdDB.add')
    def test_add_fd(self, mock_add):
        fds = FDs(TestConfig)
        fds.add({
            'bank_name': 'bank1',
            'bank_branch': 'branch1',
            'first_name': 'FirstName',
            'joint_name': '',  # Optional
            'mode': 'Ei/Sur',
            'type': 'Quarterly',
            'interest_account': 'accountNumber1',  # Optional
            'fd_number': 'FdNumber1',
            'start_date': datetime.datetime(2019, 1, 1),
            'end_date': datetime.datetime(2020, 1, 2),
            'period': '1 year 1 day',
            'roi': 8.25,
            'princpal_amount': 5000.0,
            'maturity_amount': 5000.0,
        }, for_user='u1')

        mock_add.assert_called_with(new_fd={
            'bank_name': 'bank1',
            'bank_branch': 'branch1',
            'first_name': 'FirstName',
            'joint_name': '',
            'mode': 'Ei/Sur',
            'type': 'Quarterly',
            'interest_account': 'accountNumber1',
            'fd_number': 'FdNumber1',
            'start_date': '20190101',
            'end_date': '20200102',
            'period': '1 year 1 day',
            'roi': 8.25,
            'princpal_amount': 5000.0,
            'maturity_amount': 5000.0,
            'username': 'u1',
        })

    @patch('pa.db.fd.FdDB.get_all_fds')
    def test_get_all_fds(self, mock_get_all_fds):
        fd1 = {'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName', 'joint_name': '',
               'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber1', 'fd_number': 'FdNumber1',
               'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
               'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        fd2 = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName', 'joint_name': '',
               'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'FdNumber2',
               'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
               'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        fd3 = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName', 'joint_name': '',
               'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'FdNumber3',
               'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
               'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        fd1_without_username = {'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName',
                                'joint_name': '', 'mode': 'Ei/Sur', 'type': 'Quarterly',
                                'interest_account': 'accountNumber1', 'fd_number': 'FdNumber1',
                                'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day',
                                'roi': 8.25, 'princpal_amount': 5000.0, 'maturity_amount': 5000.0, }

        fd2_without_username = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName',
                                'joint_name': '', 'mode': 'Ei/Sur', 'type': 'Quarterly',
                                'interest_account': 'accountNumber2', 'fd_number': 'FdNumber2',
                                'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day',
                                'roi': 8.25, 'princpal_amount': 5000.0, 'maturity_amount': 5000.0, }

        fd3_without_username = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName',
                                'joint_name': '', 'mode': 'Ei/Sur', 'type': 'Quarterly',
                                'interest_account': 'accountNumber2', 'fd_number': 'FdNumber3',
                                'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day',
                                'roi': 8.25, 'princpal_amount': 5000.0, 'maturity_amount': 5000.0, }

        fds = FDs(TestConfig)
        mock_get_all_fds.return_value = [fd1, fd2, fd3]
        self.assertEqual([fd1_without_username, fd2_without_username, fd3_without_username],
                         fds.get_all_fds(for_user='u1'))

    @patch('pa.db.fd.FdDB.delete_fd')
    def test_add_fd(self, mock_delete):
        fds = FDs(TestConfig)
        fds.delete_fd(fd_number='fd1', bank_name='b1', bank_branch='br1', for_user='u1')
        mock_delete.assert_called_with(fd_number='fd1', bank_name='b1', bank_branch='br1', for_user='u1')
