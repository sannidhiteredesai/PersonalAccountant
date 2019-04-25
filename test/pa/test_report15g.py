from unittest import TestCase
from pa.pa.report15g import *
from datetime import date


# class TestInterest(TestCase):
#     def test_cumulative_interest(self):
#         self.assertEqual(2, get_cumulative_interest(principal=47380, roi=7.1,
#                                                      start_date=date(18, 9, 26), end_date=date(20, 4, 3)))

class TestPeriodBetween(TestCase):
    def test_end_date_less_or_equal_to_start_date(self):
        self.assertEqual([], get_period_between(date(2019, 12, 31), date(2018, 3, 1)))
        self.assertEqual([], get_period_between(date(2019, 12, 31), date(2019, 12, 31)))

    def test_dates_in_same_month(self):
        self.assertEqual([Days(9)], get_period_between(date(2019, 1, 1), date(2019, 1, 10)))
        self.assertEqual([Days(1)], get_period_between(date(2019, 1, 12), date(2019, 1, 13)))
        self.assertEqual([Days(6)], get_period_between(date(2019, 1, 25), date(2019, 1, 31)))

    def test_dates_with_start_of_month_in_year(self):
        self.assertEqual([Months(1)], get_period_between(date(2019, 1, 1), date(2019, 2, 1)))
        self.assertEqual([Months(3)], get_period_between(date(2019, 1, 1), date(2019, 4, 1)))

    def test_dates_in_same_year(self):
        self.assertEqual([Days(1)], get_period_between(date(2019, 1, 29), date(2019, 1, 30)))
        self.assertEqual([Days(period=3),
                          Months(period=1),
                          Days(period=29)], get_period_between(date(2019, 1, 29), date(2019, 3, 30)))

    def test_dates_in_different_years(self):
        self.assertEqual([Days(3)], get_period_between(date(2018, 12, 29), date(2019, 1, 1)))
        self.assertEqual([Days(7)], get_period_between(date(2018, 12, 29), date(2019, 1, 5)))
        self.assertEqual([Days(3),
                          Months(period=1),
                          Days(period=2)], get_period_between(date(2018, 12, 29), date(2019, 2, 3)))
