from copy import deepcopy as copy_of

class FDCollection:
    
    def __init__(self):
        self.fds = []

    def add(self, new_fd):
        if new_fd in self.fds:
            raise __class__.AlreadyExistsException
        self.fds.append(new_fd)


    def exists(self, new_fd):
        return new_fd in self.fds


    def get_all_fds(self):
        return copy_of(self.fds)


    class AlreadyExistsException(Exception):
        pass

