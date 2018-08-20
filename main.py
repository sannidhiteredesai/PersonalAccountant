"""
    Personal Accountant Software
"""

from pa.fd import FDCollection

def main_function():
    """
        This is the main entry point of code that calls required
        modules/methods
    """

    fd_collection = FDCollection()
    option = 'y'
    while option in ('y', 'Y'):

        fd = {}
        fd['bank'] = input('Enter bank: ')
        fd['branch'] = input('Enter branch: ')
        fd['first_name'] = input('Enter first_name: ')
        fd['joint_name'] = input('Enter joint_name: ')
        fd['mode = input'] = ('Enter mode: ')
        fd['fd_number'] = input('Enter number: ')
        fd['auto_renewal'] = input('Enter auto_renewal: ')
        fd['start_date'] = input('Enter start_date: ')
        fd['end_date'] = input('Enter end_date: ')
        fd['period'] = input('period: ')
        fd['roi_pcpa'] = input('roi_pcpa: ')
        fd['principal_amt'] = input('principal_amt: ')
        fd['maturity_amt'] = input('maturity_amt: ')
        fd['nomination'] = input('nomination: ')

        fd_collection.add(fd)
        print(repr(fd_collection.get_all_fds()))

        option = input('Continue? (y=yes): ')

    print('Thank You')

if __name__ == '__main__':
    main_function()
