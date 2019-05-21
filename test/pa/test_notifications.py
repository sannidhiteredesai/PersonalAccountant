from unittest import TestCase
from pa.pa.fd import FDs
from pa.pa.notifications import get_maturing_fds
from unittest.mock import patch


class TestConfig:
    DB = 'memory'


class TestMaturingFDs(TestCase):

    @patch('pa.pa.fd.FDs.get_all_fds_till_date')
    def test_get_all_fds_till_date(self, mock_get_all_fds_till_date):
        fds = FDs(TestConfig)
        fd1 = {'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName1',
               'joint_name': '', 'mode': 'Ei/Sur', 'type': 'Quarterly',
               'interest_account': 'accountNumber1', 'fd_number': 'FdNumber1',
               'start_date': '20190101', 'end_date': '20190501', 'period': '1 year 1 day',
               'roi': 8.25, 'principal_amount': 5000.0, 'maturity_amount': 5000.0, }
        fd2 = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName2',
               'joint_name': '', 'mode': 'Ei/Sur', 'type': 'Quarterly',
               'interest_account': 'accountNumber1', 'fd_number': 'FdNumber2',
               'start_date': '20190101', 'end_date': '20190505', 'period': '1 year 1 day',
               'roi': 8.25, 'principal_amount': 5000.0, 'maturity_amount': 5000.0, }
        mock_get_all_fds_till_date.return_value = [fd1, fd2]

        self.assertEqual([
            {
                'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName1',
                'fd_number': 'FdNumber1', 'end_date': '20190501',
            },{
                'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName2',
                'fd_number': 'FdNumber2', 'end_date': '20190505',
            }
        ], get_maturing_fds(for_user='u1', till_date='20190505'))
