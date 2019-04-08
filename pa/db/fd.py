from tinydb import Query
from pa import get_db
from pa.config import Config


class FdDB:
    def __init__(self, config=Config):
        self.db = get_db(config).table('fds')

    def add(self, new_fd):
        self.db.insert(new_fd)

    def get_all_fds(self, for_user):
        return self.db.search(Query().username == for_user)
