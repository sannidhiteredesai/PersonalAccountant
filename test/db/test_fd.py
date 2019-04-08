from unittest import TestCase
from pa.db.fd import FdDB


class TestConfig:
    DB = 'memory'


class TestBankDB(TestCase):

    def setUp(self):
        self.fds = FdDB(config=TestConfig)

    def test_add_and_get_all_fds_for_user(self):
        fd1_u1 = {'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName', 'joint_name': '',
                  'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber1', 'fd_number': 'FdNumber1',
                  'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
                  'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        fd1_u2 = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName', 'joint_name': '',
                  'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'FdNumber2',
                  'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
                  'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u2', }

        fd2_u2 = {'bank_name': 'bank2', 'bank_branch': 'branch2', 'first_name': 'FirstName', 'joint_name': '',
                  'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'FdNumber3',
                  'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
                  'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u2', }

        self.fds.add(new_fd=fd1_u1)
        self.fds.add(new_fd=fd1_u2)
        self.fds.add(new_fd=fd2_u2)

        self.assertEqual([fd1_u1], self.fds.get_all_fds(for_user='u1'))
        self.assertEqual([fd1_u2, fd2_u2], self.fds.get_all_fds(for_user='u2'))
        self.assertEqual([], self.fds.get_all_fds(for_user='u3'))

    def test_delete_fd_for_user(self):
        fd1_u1 = {'bank_name': 'bank1', 'bank_branch': 'branch1', 'first_name': 'FirstName', 'joint_name': '',
                  'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'fd1',
                  'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
                  'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        fd2_u1 = {'bank_name': 'bank1', 'bank_branch': 'branch2', 'first_name': 'FirstName', 'joint_name': '',
                  'mode': 'Ei/Sur', 'type': 'Quarterly', 'interest_account': 'accountNumber2', 'fd_number': 'fd2',
                  'start_date': '20190101', 'end_date': '20200102', 'period': '1 year 1 day', 'roi': 8.25,
                  'princpal_amount': 5000.0, 'maturity_amount': 5000.0, 'username': 'u1', }

        self.fds.add(new_fd=fd1_u1)
        self.fds.add(new_fd=fd2_u1)
        self.assertEqual([fd1_u1, fd2_u1], self.fds.get_all_fds(for_user='u1'))

        self.fds.delete_fd(fd_number='fd2', bank_name='bank1', bank_branch='branch2', for_user='u1')
        self.assertEqual([fd1_u1], self.fds.get_all_fds(for_user='u1'))

