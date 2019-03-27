from pa.db.member import MemberDB
from pa.config import Config

class Members:
    def __init__(self, config=Config):
        self.members = MemberDB(config)

    def add(self, member, for_user):
        self.members.add(member, for_user)

    def exists(self, member, for_user):
        return self.members.exists(member, for_user)

    def get_members_of_user(self, user):
        """Returns sorted list of members"""
        members = []
        for member in self.members.get_members(for_user=user):
            if 'membername' in member:
                members.append(member['membername'])
        return sorted(members)