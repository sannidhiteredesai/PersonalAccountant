from pa.config import Config
from pa.db.fd import FdDB


class FDs:
    def __init__(self, config=Config):
        self.fds = FdDB(config)

    def add(self, fd, for_user):
        fd['start_date'] = self.date_to_str(fd['start_date'])
        fd['end_date'] = self.date_to_str(fd['end_date'])
        fd['username'] = for_user
        self.fds.add(new_fd=fd)

    def get_all_fds(self, for_user):
        fds = self.fds.get_all_fds(for_user=for_user)
        for fd in fds:
            del fd['username']
        return fds

    @staticmethod
    def date_to_str(datetime_object):
        return datetime_object.strftime("%Y%m%d")