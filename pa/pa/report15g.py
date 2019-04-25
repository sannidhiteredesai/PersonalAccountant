import collections
from pa.pa.fd import FDs
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

Months = collections.namedtuple('Months', ['period'])
Days = collections.namedtuple('Days', ['period'])


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


def get_period_between(date1, date2):  # Including date1 & Excluding date2
    if date1 >= date2:
        return []

    if date2.year == date1.year and date2.month == date1.month:
        return [Days(date2.day - date1.day)]

    period = []
    next_month_start = (date1 + relativedelta(months=1)).replace(day=1) if date1.day != 1 else date1

    days_till_next_month = (next_month_start - date1).days if date1.day != 1 else 0
    months_till_end_date = (date2.year - next_month_start.year) * 12 + \
                           date2.month - next_month_start.month
    days_in_end_month = date2.day - 1

    if days_till_next_month: period.append(Days(days_till_next_month))
    if months_till_end_date: period.append(Months(months_till_end_date))
    if days_in_end_month: period.append(Days(days_in_end_month))

    if len(period) == 2 and isinstance(period[0], Days) and isinstance(period[1], Days):
        period = [Days(period[0].period + period[1].period)]

    return period


def get_principal_at_end_of_period(principal, roi, period_before_fy):
    for period in period_before_fy:
        if isinstance(period, Days):
            principal = calculate_maturity_amount(principal=principal, roi=roi, period=period.period,
                                                  tenurePeriodVal=365, frequencyVal=4)
        if isinstance(period, Months):
            principal = calculate_maturity_amount(principal=principal, roi=roi, period=period.period,
                                                  tenurePeriodVal=12, frequencyVal=4)
    return principal


def get_cumulative_interest(principal, roi, start_date, end_date):
    year = 2019
    fy_start = date(year, 4, 1)
    next_fy_start = date(year + 1, 4, 1)

    relative_fd_start = fy_start if start_date < fy_start else start_date
    relative_fd_end = next_fy_start if end_date >= next_fy_start else end_date

    period_before_fy = get_period_between(start_date, relative_fd_start)
    new_principal = get_principal_at_end_of_period(principal, roi, period_before_fy)

    period_in_fy = get_period_between(relative_fd_start, relative_fd_end)
    return round(get_principal_at_end_of_period(new_principal, roi, period_in_fy) - new_principal, 2)


def get_quarterly_interest(principal, roi, start_date, end_date):
    year = 2019
    fy_start = date(year, 4, 1)
    next_fy_start = date(year + 1, 4, 1)

    relative_fd_start = fy_start if start_date < fy_start else start_date
    relative_fd_end = next_fy_start if end_date >= next_fy_start else end_date
    period = get_period_between(relative_fd_start, relative_fd_end)

    interest = 0
    for p in period:
        if isinstance(p, Months):
            interest += calculate_maturity_amount(principal=principal,
                                                  roi=roi,
                                                  period=p.period,
                                                  tenurePeriodVal=12,
                                                  frequencyVal=0) - principal
        elif isinstance(p, Days):
            interest += calculate_maturity_amount(principal=principal,
                                                  roi=roi,
                                                  period=p.period,
                                                  tenurePeriodVal=365,
                                                  frequencyVal=0) - principal
    return round(interest, 2)


def generate_15g_report(for_member, for_user):
    # TODO - refactoring
    fds = FDs()
    fds_for_member = fds.get_fds_with_first_name(first_name=for_member, for_user=for_user)

    bank_wise_details = {}
    total_interest_all_branches = 0
    for fd in fds_for_member:
        if fd['type'] == 'Cumulative':
            interest = get_cumulative_interest(principal=fd['principal_amount'], roi=fd['roi'],
                                               start_date=datetime.strptime(fd['start_date'], "%Y%m%d").date(),
                                               end_date=datetime.strptime(fd['end_date'], "%Y%m%d").date())
        elif fd['type'] == 'Quarterly':
            interest = get_quarterly_interest(principal=fd['principal_amount'], roi=fd['roi'],
                                              start_date=datetime.strptime(fd['start_date'], "%Y%m%d").date(),
                                              end_date=datetime.strptime(fd['end_date'], "%Y%m%d").date())

        total_interest_all_branches += interest

        entry = (fd['fd_number'], 'Interest', '194A', interest)
        if (fd['bank_name'], fd['bank_branch']) not in bank_wise_details:
            bank_wise_details[(fd['bank_name'], fd['bank_branch'])] = [entry]
        else:
            bank_wise_details[(fd['bank_name'], fd['bank_branch'])] += [entry]

    bank_wise_details = collections.OrderedDict(sorted(bank_wise_details.items()))

    total_15g_forms = len(bank_wise_details)
    this_15g_form = 1
    formatted_15g_report_details = []
    for bank_and_branch, fds in bank_wise_details.items():
        this_branch_interest = sum(map(lambda x: x[3], fds))
        formatted_15g_report_details.append({
            'bank_name': bank_and_branch[0],
            'bank_branch': bank_and_branch[1],
            'income_in_this_declaration': round(this_branch_interest, 2),
            'total_income_in_fy': round(total_interest_all_branches, 2),
            'other_15g_form_count': total_15g_forms - this_15g_form,
            'other_15g_form_income': round(total_interest_all_branches - this_branch_interest, 2),
            'fds': fds,
        })

    return formatted_15g_report_details


if __name__ == '__main__':
    generate_15g_report(for_member='aa', for_user='u')
