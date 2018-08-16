import pytest
from pa.fd import FDCollection


@pytest.fixture
def new_fd():
    return {
        'bank': 'bank1',
        'branch': 'branch1',
        'first_name': 'customer1',
        'joint_name': 'customer2',
        'mode': 'single',
        'number': 'FD1',
        'auto_renewal': True,
        'start_date': '',
        'end_date': '',
        'period': '',
        'roi_pcpa': 0,
        'principal_amt': 0,
        'maturity_amt': 0,
        'nomination': '',
    }


def test_new_fd_is_added():
    fd_collection = FDCollection()
    fd_collection.add(new_fd)
    assert fd_collection.exists(new_fd) == True, "New FD was not added"


def test_add_existing_fd_raises_exception():
    with pytest.raises(FDCollection.AlreadyExistsException):
        fd_collection = FDCollection()
        fd_collection.add(new_fd)
        fd_collection.add(new_fd)


def test_get_all_fds():
    fd_collection = FDCollection()
    assert fd_collection.get_all_fds() == []
    fd_collection.add(new_fd)
    assert fd_collection.get_all_fds() == [new_fd]
