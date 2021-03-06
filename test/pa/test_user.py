from datetime import datetime
from unittest import TestCase
from pa.pa.user import User


class TestUser(TestCase):

    def test_user_transformations(self):
        user = User({
            'username': 'user1',
            'password': 'password',
            'mobile': '1234567890',
            'dob': datetime(1991, 1, 2),
            'secret_question': 'Some question ?',
            'answer': 'Some Answer',
        })
        self.assertTrue(1234567890, user.mobile)
        self.assertTrue('02/01/1991', user.dob)
