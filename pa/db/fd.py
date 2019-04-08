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

    def delete_fd(self, fd_number, bank_name, bank_branch, for_user):
        self.db.remove((where('fd_number') == fd_number) &
                       (where('bank_name') == bank_name) &
                       (where('bank_branch') == bank_branch) &
                       (where('username') == for_user))
