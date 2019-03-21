from unittest import TestCase
from pa.db.user import UserDB
from pa.pa.user import User
import datetime

class TestConfig:
    DB = 'memory'


class TestUserDB(TestCase):

    def setUp(self):
        self.users = UserDB(config=TestConfig)

    def test_add_and_exists_user(self):
        self.users.add(User(dict(username='user1',
                                 password='password1',
                                 mobile='1234567891',
                                 dob=datetime.datetime(1991,1,1),
                                 question='Some question1',
                                 answer='Some answer1')))
        self.assertTrue(self.users.exists(username='user1'))

        self.users.add(User(dict(username='user2',
                                 password='password2',
                                 mobile='1234567892',
                                 dob=datetime.datetime(1991,1,2),
                                 question='Some question2',
                                 answer='Some answer2')))
        self.assertTrue(self.users.exists(username='user2'))

    def test_check_credentials(self):
        self.users.add(User(dict(username='user1',
                                 password='password1',
                                 mobile='1234567891',
                                 dob=datetime.datetime(1991,1,1),
                                 question='Some question1',
                                 answer='Some answer1')))
        self.assertTrue(self.users.check_credentials(username='user1', password='password1'))
        self.assertFalse(self.users.check_credentials(username='user1', password='password2'))
