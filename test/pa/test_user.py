from unittest import TestCase
from pa.pa.user import User
from datetime import datetime

class TestUser(TestCase):

    def test_user_exists(self):
        user = User({
            'username': 'user1',
            'password': 'password',
            'mobile': '1234567890',
            'dob': datetime(1991, 1, 2),
            'secret_question': 'Some question ?',
            'answer': 'Some nswer',
        })
        self.assertTrue(1234567890, user.mobile)
        self.assertTrue('02/01/1991', user.dob)
