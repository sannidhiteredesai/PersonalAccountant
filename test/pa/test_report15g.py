from unittest import TestCase
from unittest.mock import patch

from pa.pa.report15g import *


class TestReport15G(TestCase):

    def test_get_nearest_start_of_month(self):
        self.assertEqual(datetime.date(2019, 3, 1), get_nearest_start_of_month(datetime.date(2019, 3, 1)))
        self.assertEqual(datetime.date(2019, 3, 1), get_nearest_start_of_month(datetime.date(2019, 3, 10)))
        self.assertEqual(datetime.date(2019, 3, 1), get_nearest_start_of_month(datetime.date(2019, 3, 15)))
        self.assertEqual(datetime.date(2019, 3, 1), get_nearest_start_of_month(datetime.date(2019, 3, 16)))

        self.assertEqual(datetime.date(2019, 4, 1), get_nearest_start_of_month(datetime.date(2019, 3, 17)))
        self.assertEqual(datetime.date(2019, 4, 1), get_nearest_start_of_month(datetime.date(2019, 3, 20)))
        self.assertEqual(datetime.date(2019, 4, 1), get_nearest_start_of_month(datetime.date(2019, 3, 25)))
        self.assertEqual(datetime.date(2019, 4, 1), get_nearest_start_of_month(datetime.date(2019, 3, 31)))

    # def test_start_date_less_than_fy(self):
    #     self.assertEqual(4466.20, get_interest_for_next_year(principal=1000,
    #                                                          roi=7.56,
    #                                                          start_date='20190101',
    #                                                          end_date='20210101'))
