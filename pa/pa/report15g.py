from pa.pa.fd import FDs
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


def get_nearest_start_of_month(date):
    first_day_of_this_month = date + relativedelta(day=1)
    first_day_of_next_month = date + relativedelta(day=1, months=+1)
    before_days = date - first_day_of_this_month
    after_days = first_day_of_next_month - date
    return first_day_of_this_month if before_days <= after_days else first_day_of_next_month


def number_of_months(date1, date2):
    # TODO - take a param include_last_month
    if date1.year == date2.year:
        months = date2.month - date1.month + 1
    else:
        months = (date2.year - date1.year) * 12 + date2.month - date1.month + 1
    return months if months > 0 else 0


# def get_interest_for_next_year(principal, roi, start_date, end_date):
#     year_start = datetime.datetime.utcnow().strftime("%Y")+'0401'
#     year_end = str(int(datetime.datetime.utcnow().strftime("%Y"))+1)+'0331'
#     print(year_start)
#     print(year_end)
#     return 0
#
def calculate_maturity_amount(principal, roi, period, tenurePeriodVal=12, frequencyVal=4):
    # TODO - write tests for this function, refactor te function

    if period < 90 and tenurePeriodVal == 365:
        frequencyVal = 0

    if frequencyVal == 0:  # Simple Interest
        fdMatVal = principal * (1 + ((roi * period) / (tenurePeriodVal * 100)))

    else:  # Compound Interest
        val1 = 1 + roi / (100 * frequencyVal)
        val2 = (period * frequencyVal / tenurePeriodVal)
        val3 = pow(val1, val2)
        fdMatVal = (principal * val3)

    return round(fdMatVal, 2)


def get_interest_in_next_year(principal, roi, start_date):
    # TODO - take type 'Cumulative/Simple' as the input, currently only cumulative is supported
    # TODO - make the function more robust, using proper number of months
    # TODO - The year below should be dynamic
    year = 2019
    fy_start_month = date(year, 4, 1)
    fy_end_month = date(year + 1, 3, 1)

    if start_date < fy_start_month:
        relative_start_date = get_nearest_start_of_month(start_date)
        months_in_previous_fy = number_of_months(relative_start_date, fy_start_month) - 1
        new_principal = calculate_maturity_amount(principal=principal, roi=roi, period=months_in_previous_fy)
        return calculate_maturity_amount(principal=new_principal, roi=roi, period=12)
    else:
        new_start_date = get_nearest_start_of_month(start_date)
        period = number_of_months(new_start_date, fy_end_month)
        return calculate_maturity_amount(principal=principal, roi=roi, period=period)


def generate_15g_report(for_member, for_user):
    fds = FDs()
    fds_for_member = fds.get_fds_with_first_name(first_name=for_member, for_user=for_user)
    for fd in fds_for_member:
        if fd['type'] == 'Cumulative':
            print(get_interest_in_next_year(principal=fd['principal_amount'],
                                            roi=fd['roi'],
                                            start_date=datetime.datetime.strptime(fd['start_date'], "%Y%m%d").date()))


if __name__ == '__main__':
    generate_15g_report(for_member='aa', for_user='u')
