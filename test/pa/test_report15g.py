from unittest import TestCase
from pa.pa.report15g import *
import pa.pa.report15g as report15g
from datetime import date
import datetime


class MockDateTime(datetime.datetime):
    @classmethod
    def now(cls): return cls(2019, 1, 1)


report15g.datetime = MockDateTime


class TestInterest(TestCase):

    def test_cumulative_interest(self):
        # start_date = fy and end_date = next_fy
        self.assertEqual(103.81, get_cumulative_interest(principal=1000, roi=10,
                                                         start_date=date(2019, 4, 1),
                                                         end_date=date(2020, 4, 1)))

        # start_date < fy and end_date < next_fy
        self.assertEqual(8.27, get_cumulative_interest(principal=1000, roi=10,
                                                       start_date=date(2019, 3, 29),
                                                       end_date=date(2019, 5, 1)))

        # start_date < fy and end_date > next_fy
        self.assertEqual(103.9, get_cumulative_interest(principal=1000, roi=10,
                                                        start_date=date(2019, 3, 29),
                                                        end_date=date(2020, 5, 2)))

        # start_date > fy and end_date < next_fy
        self.assertEqual(21.62, get_cumulative_interest(principal=1000, roi=10,
                                                        start_date=date(2019, 4, 20),
                                                        end_date=date(2019, 7, 8)))

        # start_date > fy and end_date > next_fy
        self.assertEqual(98.06, get_cumulative_interest(principal=1000, roi=10,
                                                        start_date=date(2019, 4, 20),
                                                        end_date=date(2020, 5, 20)))

    def test_quarterly_interest(self):
        # start_date = fy and end_date = next_fy
        self.assertEqual(100, get_quarterly_interest(principal=1000, roi=10,
                                                     start_date=date(2019, 4, 1),
                                                     end_date=date(2020, 4, 1)))

        # start_date < fy and end_date < next_fy
        self.assertEqual(8.33, get_quarterly_interest(principal=1000, roi=10,
                                                      start_date=date(2019, 3, 29),
                                                      end_date=date(2019, 5, 1)))

        # start_date < fy and end_date > next_fy
        self.assertEqual(100, get_quarterly_interest(principal=1000, roi=10,
                                                     start_date=date(2019, 3, 29),
                                                     end_date=date(2020, 5, 2)))

        # start_date > fy and end_date < next_fy
        self.assertEqual(21.6, get_quarterly_interest(principal=1000, roi=10,
                                                      start_date=date(2019, 4, 20),
                                                      end_date=date(2019, 7, 8)))

        # start_date > fy and end_date > next_fy
        self.assertEqual(94.68, get_quarterly_interest(principal=1000, roi=10,
                                                       start_date=date(2019, 4, 20),
                                                       end_date=date(2020, 5, 20)))


class TestPeriodBetween(TestCase):

    def compare(self, expected_period, actual_period):
        assertion_error = f'{expected_period} != {actual_period}'
        if expected_period != actual_period: raise AssertionError(assertion_error)
        for e, a in zip(expected_period, actual_period):
            if type(e) != type(a): raise AssertionError(assertion_error)
        return True

    def test_end_date_less_or_equal_to_start_date(self):
        self.compare([], get_period_between(date(2019, 12, 31), date(2018, 3, 1)))
        self.compare([], get_period_between(date(2019, 12, 31), date(2019, 12, 31)))

    def test_dates_in_same_month(self):
        self.compare([Days(9)], get_period_between(date(2019, 1, 1), date(2019, 1, 10)))
        self.compare([Days(1)], get_period_between(date(2019, 1, 12), date(2019, 1, 13)))
        self.compare([Days(6)], get_period_between(date(2019, 1, 25), date(2019, 1, 31)))

    def test_dates_with_start_of_month_in_year(self):
        self.compare([Months(1)], get_period_between(date(2019, 1, 1), date(2019, 2, 1)))
        self.compare([Months(3)], get_period_between(date(2019, 1, 1), date(2019, 4, 1)))

    def test_dates_in_same_year(self):
        self.compare([Days(1)], get_period_between(date(2019, 1, 29), date(2019, 1, 30)))
        self.compare([Days(3), Months(1), Days(29)], get_period_between(date(2019, 1, 29), date(2019, 3, 30)))

    def test_dates_in_different_years(self):
        self.compare([Days(3)], get_period_between(date(2018, 12, 29), date(2019, 1, 1)))
        self.compare([Days(7)], get_period_between(date(2018, 12, 29), date(2019, 1, 5)))
        self.compare([Days(3), Months(1), Days(2)], get_period_between(date(2018, 12, 29), date(2019, 2, 3)))


class TestFinancialYear(TestCase):
    def test_get_financial_year(self):
        self.assertEqual(2019, get_financial_year()[0])
        self.assertEqual(2020, get_financial_year()[1])
