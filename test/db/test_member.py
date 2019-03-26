from unittest import TestCase
from pa.db.member import MemberDB


class TestConfig:
    DB = 'memory'


class TestUserDB(TestCase):

    def setUp(self):
        self.members = MemberDB(config=TestConfig)

    def test_add_and_exists_member(self):
        self.members.add(member='m1', for_user='u1')
        self.assertTrue(self.members.exists(member='m1', for_user='u1'))
        self.assertFalse(self.members.exists(member='m2', for_user='u1'))

    def test_get_all_members(self):
        self.assertEquals(self.members.get_members(for_user='u1'), [])

        self.members.add(member='m1', for_user='u1')
        self.assertEquals(self.members.get_members(for_user='u1'), [{'membername': 'm1', 'username': 'u1'}])

        self.members.add(member='m2', for_user='u1')
        self.assertEquals(self.members.get_members(for_user='u1'), [{'membername': 'm1', 'username': 'u1'},
                                                                    {'membername': 'm2', 'username': 'u1'}])
