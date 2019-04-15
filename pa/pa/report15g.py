from pa.pa.fd import FDs
import datetime
from dateutil.relativedelta import relativedelta

def get_nearest_start_of_month(date):
    first_day_of_this_month = date + relativedelta(day=1)
    first_day_of_next_month = date + relativedelta(day=1, months=+1)
    before_days = date - first_day_of_this_month
    after_days = first_day_of_next_month - date
    return first_day_of_this_month if before_days <= after_days else first_day_of_next_month

def number_of_months(date1, date2):
    return (date2.year - date1.year) * 12 + date2.month - date1.month + 1

# def get_interest_for_next_year(principal, roi, start_date, end_date):
#     year_start = datetime.datetime.utcnow().strftime("%Y")+'0401'
#     year_end = str(int(datetime.datetime.utcnow().strftime("%Y"))+1)+'0331'
#     print(year_start)
#     print(year_end)
#     return 0
#
def generate_15g_report(for_member, for_user):
    fds = FDs()
    print(fds.get_all_fds(for_user='u'))
    fds_for_member = fds.get_fds_with_first_name(first_name=for_member, for_user=for_user)

    print(str(fds_for_member))
    for fd in fds_for_member:
        print(fd)
#
# if __name__ == '__main__':
#     generate_15g_report(for_member='aa', for_user='u')