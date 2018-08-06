import pytest
import pa.fd as fd


def test_new_fd_is_added():
    new_fd = {
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
    fd.add(new_fd)
    assert fd.exists(new_fd) == True, "New FD was not added"


def test_add_existing_fd_raises_exception():
    with pytest.raises(fd.AlreadyExistsException):
        new_fd = {
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
        fd.add(new_fd)
        fd.add(new_fd)
