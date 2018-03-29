import unittest
import random #import the unittest module
from credentials import user

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
        self.new_user = user("name","pwd")

    def test_init(self):
        '''
        test if object is initializd correctly
        '''
        self.assertEqual(self.new_user.pwd,"pwd")

    def test_save_pwd(self):
        '''
        test if password entered is saved
        '''
        self.new_user.save_user() #saving new user
        self.assertEqual(len(user.user_list),1)

    def test_generate_password(self):
        '''
        test to auto-generate password
        '''
        self.new_user.generate_password() #generating new password
        self.assertEqual(self.new_user.pwd,"pwd")

if __name__ == '__main__':
    unittest.main()
