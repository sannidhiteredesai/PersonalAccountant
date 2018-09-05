import pytest
from pa.bank import BankCollection, \
                    Day, \
                    Time

def test_get_all_banks():
    banks = BankCollection()
    assert banks.get_all_bank_details() == []

def test_add_empty_bank_raises_exception():
    with pytest.raises(BankCollection.InsufficientInformation):
        banks = BankCollection()
        banks.add({})

def test_insufficient_information_exception():
    with pytest.raises(BankCollection.InsufficientInformation):
        banks = BankCollection()
        banks.add({
            'bank_branch': '',
            'bank_address': '',
            'bank_timings': '',
        })  # bank_name is missing


def test_timing_must_be_in_12_hour_clock_format():
    with pytest.raises(BankCollection.InValidBankTimings):
        banks = BankCollection()
        bank_open_on = [(Day.MONDAY, '20:30', Time.AM, '1:30', Time.PM)]
        banks.add({
            'bank_name': 'ABC Bank',
            'bank_branch': 'ABC Branch',
            'bank_address': 'Address of bank',
            'bank_timings': bank_open_on,
        })


def test_open_time_is_before_close_time():
    with pytest.raises(BankCollection.InValidBankTimings):
        banks = BankCollection()
        bank_open_on = [(Day.MONDAY, '9:30', Time.AM, '8:30', Time.AM)]
        banks.add({
            'bank_name': 'ABC Bank',
            'bank_branch': 'ABC Branch',
            'bank_address': 'Address of bank',
            'bank_timings': bank_open_on,
        })


def test_add_valid_bank_is_successful():
    banks = BankCollection()
    
    bank_open_on = [(Day.MONDAY, '8:30', Time.AM, '12:30', Time.PM)]
    bank = {
        'bank_name': 'ABC Bank',
        'bank_branch': 'ABC Branch',
        'bank_address': 'Address of bank',
        'bank_timings': bank_open_on,
    }
    banks.add(bank)

    assert banks.get_all_bank_details()[0] == bank
