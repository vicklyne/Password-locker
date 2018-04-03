import unittest #import the unittest module
import pyperclip
from credential import credentials #importing credentials class

class TestCredentials(unittest.TestCase):
    '''
    defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_account = credentials("Account","Testname","TestPass")

    def tearDown(self):
        '''
        clean up after each test case has run
        '''
        credentials.credential_list = []

    def test_init(self):
        '''
        test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Account")
        self.assertEqual(self.new_account.user_name,"Testname")
        self.assertEqual(self.new_account.password,"TestPass")

    def test_save_account(self):
        '''
        test if the account is saved into the credentials list
        '''
        self.new_account.save_account()
        self.assertEqual(len(credentials.credential_list),1)

    def test_save_multiple_accounts(self):
        '''
        test to check if one can save multiple accounts
        '''
        self.new_account.save_account()
        test_account = credentials("Account","Testname","TestPass")
        test_account.save_account()
        self.assertEqual(len(credentials.credential_list),2)

    def test_delete_credentials(self):
        '''
        test to check if one can delete account credentials
        '''
        self.new_account.save_account()
        test_account = credentials("Account","Testname","TestPass")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(credentials.credential_list),1)

    def test_find_account_by_account_name(self):
        '''
        test to search for account details
        '''
        self.new_account.save_account()
        test_account = credentials("Account","Testname","TestPass")
        test_account.save_account()
        found_account = credentials.find_by_account("Account")
        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self):
        '''
        test to check if account really exists
        '''
        self.new_account.save_account()
        test_account = credentials("Account","Testname","TestPass")
        test_account.save_account()
        account_exists = credentials.account_exists("Account")
        self.assertTrue(account_exists)

    def test_display_accounts(self):
        '''
        test to display accounts
        '''
        self.assertEqual(credentials.display_accounts(),credentials.credential_list)

if __name__ == '__main__':
    unittest.main()
