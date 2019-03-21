from unittest import TestCase
from pa.pa.user import Users

class TestUser(TestCase):

    def setUp(self):
        self.users = Users()

    # def test_user_exists(self):
    #     self.users.add()
    #     self.assertTrue(self.users.exists('user1'))
