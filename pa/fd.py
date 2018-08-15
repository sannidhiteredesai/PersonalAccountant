fds = []


def add(new_fd):
    global fds
    if new_fd in fds:
        raise AlreadyExistsException
    fds.append(new_fd)


def exists(new_fd):
    return new_fd in fds


class AlreadyExistsException(Exception):
    pass

