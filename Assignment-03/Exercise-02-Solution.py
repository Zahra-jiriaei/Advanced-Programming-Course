# Bank account
# Zahra Jiriaei

# FIRST PART
# import required library
import itertools
from decimal import Decimal
from datetime import timedelta

# Time Zone class for calculating time
class TimeZone:
    
    def __init__(self, name, offset_hours, offset_minutes):
        # Check time zone name 
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.') 
        self.name = str(name).strip()
        
        # Check time zone hour
        if type(offset_hours) != int:
            raise ValueError('Hour offset must be an integer.')
        
        # Check time zone minute ---> int
        if type(offset_minutes) != int:
            raise ValueError('Minutes offset must be an integer.')
        
        # Check time zone minute ---> be between -59 ,59
        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')
         
        # Claculating time difference between countries
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        
        # Check offest time to be between -12 and 14
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')
        
        # If given info was True, then do following
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes
        self.offset = offset
        
    # Represent a class's objects as a string.   
    def __repr__(self):
        return (f"TimeZone(name='{self.name}', offset_hours={self.offset_hours}, offset_minutes={self.offset_minutes})")

# Main class for account     
class Account:
    
    # Define counter for transaction
    transaction_counter = itertools.count(100)
    
    # Define interest_rate
    interest_rate = 0.5 
    
    # Define transaction codes abriviation
    transaction_codes = {'deposit' : 'D','withdraw' : 'W','interest' : 'I','rejected' : 'X'}
    
    def __init__(self, account_number, first_name, last_name,timezone = None, balance = Decimal('0.0')):
         
        # Check if first name and last name given
        if len(first_name) == 0: 
            raise ValueError('First name cannot be empty.')
        if len(last_name) == 0: 
            raise ValueError('Last name cannot be empty.')
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        
        # Check time zone input
        if timezone is None:
            self.timezone = TimeZone('Tehran', 3, 30)
        elif not isinstance(timezone, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object')
        else:
            self.timezone = timezone
        
        # Bank account balance ---> it must not be negative
        if balance < Decimal('0.0'):
            raise ValueError('initial balance must be a non-negative value')
        self.balance = balance
    
    # Confirmation code
    def generate_confirmation_code(self, transaction_code):
        """
        confirmation code generators function
        """
        transaction_id = next(Account.transaction_counter)
        dt_str = (datetime.utcnow()+self.timezone.offset).strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{transaction_id}'
    
    # Deposit money 
    def deposit(self, value):
        """
        Deposit money function
        """
        # Deposit money must be non negetive
        if value < Decimal('0.0'):
            raise ValueError('Deposit value must be a positive number')
            
        # Add money to bank account
        conf_code = self.generate_confirmation_code(Account.transaction_codes['deposit'])
        self.balance += value
        return conf_code
    
    # withdraw money
    def withdraw(self, value):
        """
        withdraw function
        """
        flag = False
        
        # Amount of withdraw must be non negetive
        if value < Decimal('0.0'):
            raise ValueError('withdraw value must be a positive number')
        
        # Balance must be negative after withdrawing
        if self.balance - value < Decimal('0.0'):
            transaction_code = Account.transaction_codes['rejected']
            
        # Mines money from bank account
        else:
            transaction_code = Account.transaction_codes['withdraw']
            flag = True
        conf_code = self.generate_confirmation_code(transaction_code)
        if flag:
            self.balance -= value
        return conf_code
    
    # pay_interest
    def pay_interest(self):
        """
        pay interest function
        """
        interest = self.balance * Account.interest_rate / 100
        conf_code = self.generate_confirmation_code(Account.transaction_codes['interest'])
        self.balance += interest
        return conf_code
    
# confirmation_code_parser
class confirmation_code_parser:
    def __init__(self,confirmation_code,Timezone_name):
        """
        confirmation code function
        """
        # Check confirmation_code_parser given information
        confirmation_code_list=self.confirmation_code.split("-")
        if len(confirmation_code_list) != 4:
            raise ValueError('confirmation_code is not valid')
        
        if len(Timezone_name)==0:
            raise ValueError('confirmation_code is empaty')
        
        self.confirmation_code=confirmation_code
        self.Timezone_name=Timezone_name      
        self.account_number=confirmation_code_list[1]
        self.transaction_code=confirmation_code_list[0]
        self.transaction_id=confirmation_code_list[3] 
        self.time="{}-{}-{} {}:{}:{}".format(confirmation_code_list[2][:4],
                                            confirmation_code_list[2][4:6],
                                            confirmation_code_list[2][6:8],
                                            confirmation_code_list[2][8:10],
                                            confirmation_code_list[2][10:12],
                                            confirmation_code_list[2][12:14])
        self.time_utc="{}-{}-{}T{}:{}:{}".format(confirmation_code_list[2][:4],
                                            confirmation_code_list[2][4:6],
                                            confirmation_code_list[2][6:8],
                                            confirmation_code_list[2][8:10],
                                            confirmation_code_list[2][10:12],
                                            confirmation_code_list[2][12:14])

# SECOND PART
# import unitest

import unittest
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestAccount(unittest.TestCase):
    def test_create_timezone_1(self):
        
        """
        Check time zone
        """
        
        tz = TimeZone('Arak', -1, -30)
        self.assertEqual('Arak', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)

    def test_create_account(self):
        """ 
        Check given info in account 
        """
        account_number = '45851'
        first_name = 'Zahra'
        last_name = 'Jiriaei'
        tz = TimeZone('karaj', 1, 30)
        balance = Decimal('2000')
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
            
    def test_account_withdraw_ok(self):
        """ 
        Check withdraw function
        """
        account_number = '45851'
        first_name = 'Zahra'
        last_name = 'Jiriaei'
        tz = TimeZone('karaj', 1, 30)
        balance = Decimal('2000')
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.withdraw(20)
        self.assertTrue(conf_code.startswith('W-'))
        self.assertEqual(balance-Decimal('20'), a.balance)
        
    def test_account_deposit_ok(self):
        """ 
        Check deposit function
        """
        account_number = '45851'
        first_name = 'Zahra'
        last_name = 'Jiriaei'
        tz = TimeZone('karaj', 1, 30)
        balance = Decimal('2000')
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.deposit(20)
        self.assertTrue(conf_code.startswith('D-'))
        self.assertEqual(balance-Decimal('20'), a.balance)
    
    def test_account_pay_interest_ok(self):
        """ 
        Check pay_interest function
        """
        account_number = '45851'
        first_name = 'Zahra'
        last_name = 'Jiriaei'
        tz = TimeZone('karaj', 1, 30)
        balance = Decimal('2000')
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.pay_interest()
        self.assertTrue(conf_code.startswith('I-'))
        self.assertEqual(balance-Decimal('20'), a.balance)