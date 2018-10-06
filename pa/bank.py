from copy import deepcopy as copy_of
from enum import Enum
import time

class BankCollection:

    def __init__(self):
        self.banks = []

    def get_all_bank_details(self):
        """
        This method returns details of all banks in the form [type - list(dict)]:
        list({
            'bank_name': 'value',
            'bank_branch': 'value',
            'bank_branch_code': 'value',
            'bank_address': 'value',
            'bank_timings': value,
            'bank_ifsc_code': 'value',
            'bank_micr_code': 'value',
            'bank_phone_numbers': ['value'],
            'bank_email': 'value',
            'bank_website': 'value',
        })
        """
        return copy_of(self.banks)

    def add(self, bank):
        """
        This method takes bank as an input in the form [type - dict]:
        {
            'bank_name': 'value',
            'bank_branch': 'value',
            'bank_branch_code': 'value',
            'bank_address': 'value',
            'bank_timings': value,
            'bank_ifsc_code': 'value',
            'bank_micr_code': 'value',
            'bank_phone_numbers': ['value'],
            'bank_email': 'value',
            'bank_website': 'value',
        }
        and if all the bank's details are valid then stores it in the collection
        """
        self._check_bank_has_all_details(bank)
        self._check_proper_bank_timings_on_all_days(bank['bank_timings'])
        self.banks.append(bank)

    def get_bank_open_days(self, bank_name):
        """
        This method return all the days on which given bank is open
        @param:  bank_name [type - str]
        @retuns: day_names [type - set(str)]
        """
        for bank in self.banks:
            if bank['bank_name'] == bank_name:
                return {day[0].name for day in bank['bank_timings']}
        return {}

    @staticmethod
    def _is_valid_hrs_and_mins(time_):
        """
        This method checks if the input time is in format %I:%M
        where,
            %I - Hour(12-hour-clock) as decimal[1,12]
            %M - Minutes as decimal[0,59]
        @param time_: string representing time in hours:minutes
        @return: True  - if time is in a valid format
                 False - if time is not in a valid format
        """
        try:

            time.strptime(time_, '%I:%M')
            return True
        except ValueError:
            return False

    @staticmethod
    def _time_in_24_hr(hrs_colon_mins, am_or_pm):
        """
        This method converts 12 hr clock format time to 24 hr clock format
        @param hrs_colon_mins: string in 12 hr clock format
        @param am_or_pm: string 'AM' or 'PM'
        @return: 24 hr string representation of input time
        """
        return time.strftime(
            '%H:%M',
            time.strptime(f'{hrs_colon_mins} {am_or_pm.name}', '%I:%M %p'))

    def _check_bank_has_all_details(self, bank):
        """
        This method checks if bank has all the required detail like:
            bank_name, bank_branch, bank_address, bank_timings
        @raises: InsufficientInformation Exception if missing details
        """
        missing_required_keys = any(field not in bank for field in \
                                    ['bank_name', 'bank_branch', 'bank_branch_code', \
                                     'bank_address', 'bank_timings', \
                                     'bank_ifsc_code', 'bank_micr_code', \
                                     'bank_phone_numbers', 'bank_email', 'bank_website', \
                                     ])
        if missing_required_keys:
            raise self.__class__.InsufficientInformation()

    def _check_proper_bank_timings_on_all_days(self, days):
        """
        This method checks if bank timings are valid on all days
        and checks if bank opens before it closes on all days
        @raises: InValidBankTimings Exception if invalid timings on any day
        """
        invalid_bank_timings = not all([self.__class__._is_valid_hrs_and_mins(d[1]) and \
                                        self.__class__._is_valid_hrs_and_mins(d[3]) \
                                        for d in days])
        if invalid_bank_timings:
            raise __class__.InValidBankTimings()

        closing_before_opening = any([self.__class__._time_in_24_hr(d[1], d[2]) > \
                                      self.__class__._time_in_24_hr(d[3], d[4]) \
                                      for d in days])
        if closing_before_opening:
            raise self.__class__.InValidBankTimings()

    def update(self, bank):
        for b in self.banks:
            if b['bank_name'] == bank['bank_name'] and b['bank_branch'] == bank['bank_branch']:
                b['bank_branch_code'] = bank['bank_branch_code']
                b['bank_address'] = bank['bank_address']
                b['bank_timings'] = bank['bank_timings']
                b['bank_ifsc_code'] = bank['bank_ifsc_code']
                b['bank_micr_code'] = bank['bank_micr_code']
                b['bank_phone_numbers'] = bank['bank_phone_numbers']
                b['bank_email'] = bank['bank_email']
                b['bank_website'] = bank['bank_website']

    class InsufficientInformation(Exception):
        pass

    class InValidBankTimings(Exception):
        pass

    class OverlappingBankTimings(Exception):
        pass



class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Time(Enum):
    AM = 1
    PM = 2
