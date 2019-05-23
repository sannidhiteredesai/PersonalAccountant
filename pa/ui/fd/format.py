"""
    This is a utility module
"""


def append_serial_number(all_fds):
    """
    This function will append bank wise serial number starting from 1 to every fd
    and also add the block value even/odd to it such that all fds in a bank have same block value
    :param all_fds - <list<dict>>
    :return:  None - as all_fds are modified in place
    """

    # Sort the fds bank-wise and bank-branch-wise
    all_fds.sort(key=lambda x: (x['bank_name'], x['bank_branch']))

    current_bank = all_fds[0]['bank_name'] if all_fds else ''
    serial_number = 0
    block = 'even'

    # Append the serial number to fd dict, where the serial number starts from 1 for every bank
    for f in all_fds:
        if current_bank == f['bank_name']:
            serial_number += 1
        else:
            serial_number = 1
            block = 'odd' if block == 'even' else 'even'

        current_bank = f['bank_name']
        f['serial_number'] = serial_number
        f['block'] = block
