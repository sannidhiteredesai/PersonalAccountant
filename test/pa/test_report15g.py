from datetime import date
from unittest import TestCase
from unittest.mock import patch

from pa.pa.report15g import *


class TestReport15G(TestCase):

    def test_get_nearest_start_of_month(self):
        self.assertEqual(date(2019, 3, 1), get_nearest_start_of_month(date(2019, 3, 1)))
        self.assertEqual(date(2019, 3, 1), get_nearest_start_of_month(date(2019, 3, 10)))
        self.assertEqual(date(2019, 3, 1), get_nearest_start_of_month(date(2019, 3, 15)))
        self.assertEqual(date(2019, 3, 1), get_nearest_start_of_month(date(2019, 3, 16)))

        self.assertEqual(date(2019, 4, 1), get_nearest_start_of_month(date(2019, 3, 17)))
        self.assertEqual(date(2019, 4, 1), get_nearest_start_of_month(date(2019, 3, 20)))
        self.assertEqual(date(2019, 4, 1), get_nearest_start_of_month(date(2019, 3, 25)))
        self.assertEqual(date(2019, 4, 1), get_nearest_start_of_month(date(2019, 3, 31)))

    def test_number_of_months_between_two_dates(self):
        self.assertEqual(0, number_of_months(date(2019, 4, 1), date(2018, 4, 1)))
        self.assertEqual(1, number_of_months(date(2019, 4, 1), date(2019, 4, 1)))
        self.assertEqual(3, number_of_months(date(2019, 4, 1), date(2019, 6, 1)))
        self.assertEqual(12, number_of_months(date(2019, 4, 1), date(2020, 3, 1)))
        self.assertEqual(13, number_of_months(date(2019, 4, 1), date(2020, 4, 1)))
        self.assertEqual(24, number_of_months(date(2018, 1, 1), date(2019, 12, 1)))

    # def test_start_date_less_than_fy(self):
    #     self.assertEqual(4466.20, get_interest_for_next_year(principal=1000,
    #                                                          roi=7.56,
    #                                                          start_date='20190101',
    #                                                          end_date='20210101'))
