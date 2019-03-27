from unittest import TestCase
from unittest.mock import patch

from pa.pa.member import Members


class TestConfig:
    DB = 'memory'


class TestMember(TestCase):

    def setUp(self):
        self.mock_members = [
            {'membername': 'm1', 'username': 'u1'},
            {'membername': 'm3', 'username': 'u1'},
            {'membername': 'm2', 'username': 'u1'},
        ]

    @patch('pa.db.member.MemberDB.exists')
    def test_get_all_members_is_sorted(self, mock_exists):
        members = Members(config=TestConfig)

        mock_exists.return_value = True if {'membername': 'm1', 'username': 'u1'} in self.mock_members else False
        self.assertTrue(members.exists(member='m1', for_user='u1'))

        mock_exists.return_value = True if {'membername': 'm2', 'username': 'u1'} in self.mock_members else False
        self.assertTrue(members.exists(member='m2', for_user='u1'))

        mock_exists.return_value = True if {'membername': 'm3', 'username': 'u1'} in self.mock_members else False
        self.assertTrue(members.exists(member='m3', for_user='u1'))

        mock_exists.return_value = True if {'membername': 'm4', 'username': 'u1'} in self.mock_members else False
        self.assertFalse(members.exists(member='m4', for_user='u1'))

    @patch('pa.db.member.MemberDB.add')
    def test_add_member(self, mock_add):
        members = Members(config=TestConfig)
        members.add(member='m1', for_user='u1')
        mock_add.assert_called_with('m1', 'u1')

    @patch('pa.db.member.MemberDB.get_members')
    def test_get_members_of_user(self, mock_get_members):
        members = Members(config=TestConfig)

        mock_get_members.return_value = [{'membername': 'm1', 'username': 'u1'},
                                         {'membername': 'm3', 'username': 'u1'},
                                         {'membername': 'm2', 'username': 'u1'}]
        self.assertEqual(['m1', 'm2', 'm3'], members.get_members_of_user('u1'))

        mock_get_members.return_value = [{'membername': 'm5', 'username': 'u2'},
                                         {'membername': 'm4', 'username': 'u2'}]
        self.assertEqual(['m4', 'm5'], members.get_members_of_user('u2'))

        mock_get_members.return_value = []
        self.assertEqual([], members.get_members_of_user('u3'))
