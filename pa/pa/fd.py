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

    def get_all_fds_till_date(self, for_user, till_date):
        fds = self.fds.get_all_fds_till_date(for_user=for_user, till_date=till_date)
        for fd in fds:
            del fd['username']
        fds.sort(key=lambda x:x['end_date'])
        return fds

    def get_fds_with_first_name(self, first_name, for_user):
        fds = self.fds.get_fds_with_first_name(first_name=first_name, for_user=for_user)
        for fd in fds:
            del fd['username']
        return fds

    def delete_fd(self, fd_number, bank_name, bank_branch, for_user):
        self.fds.delete_fd(fd_number=fd_number, bank_name=bank_name, bank_branch=bank_branch, for_user=for_user)

    @staticmethod
    def date_to_str(datetime_object):
        return datetime_object.strftime("%Y%m%d")