from tinydb import Query, where
from pa import get_db
from pa.config import Config


class FdDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('fds')

    def add(self, new_fd):
        self.db.insert(new_fd)

    def get_all_fds(self, for_user):
        return self.db.search(Query().username == for_user)

    def get_all_fds_till_date(self, for_user, till_date):
        print(self.get_all_fds(for_user))
        return self.db.search((where('end_date') <= till_date) & (where('username') == for_user))

    def get_fds_with_first_name(self, first_name, for_user):
        return self.db.search((where('first_name') == first_name) & (where('username') == for_user))

    def delete_fd(self, fd_number, bank_name, bank_branch, for_user):
        self.db.remove((where('fd_number') == fd_number) &
                       (where('bank_name') == bank_name) &
                       (where('bank_branch') == bank_branch) &
                       (where('username') == for_user))

    def fds_exists_for_member(self, member, for_user):
        return bool(self.db.search(((where('first_name') == member) | (where('joint_name') == member)) &
                    (where('username') == for_user)))
