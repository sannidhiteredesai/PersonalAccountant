from pa.pa.fd import FDs


def get_maturing_fds(for_user, till_date):
    fds = []
    for fd in FDs().get_all_fds_till_date(for_user=for_user, till_date=till_date):
        fds.append({
            'bank_name': fd['bank_name'],
            'bank_branch': fd['bank_branch'],
            'first_name': fd['first_name'],
            'fd_number': fd['fd_number'],
            'end_date': fd['end_date'],
        })
    return fds
