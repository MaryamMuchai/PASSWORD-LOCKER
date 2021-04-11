import unittest
from user import User
from user import Records

class UserTest(unittest.TestCase):
  '''
  test class that defines test cases for the user class
  '''
  def setUp(self):
      self.new_uset = User('User','0123')

  def tearDown(self):
      '''
      method called after each user
      '''
      User.user =[]

  def test_init(self):
       '''
       test method for correct initialization
       '''
       self.assertEqual(self.username, 'User')
       self.assertEqual(self.password, '0123')

  def test_save_user(self):
      '''
      test method if user has been saved
      '''
      self.user.save_user()
      self.assertEqual(len(User.user),1)

class Test(unittest.TestCase):
    def setUp(self):
        '''
        method for each test
        '''
        self.account_records= Records('twitter')

    def tearDown(self):
        '''
        method for each test
        '''
        Records.account_records = []

    def test_init(self):
        '''
        proper initialization
        '''
        self.assertEqual(self.account.account_records, 'twitter')
        self.assertEqual(self.account.username,'User')
        self.assertEqual(self.password,'123')

    def test_delete_account(self):
        '''
        test method for a deleted account
        '''
        self.account.save_accounts()
        another_account = Records('Twitter')
        another_account.delete_account()

    def test_password_generate(self):
        '''
        test method for auto generate passwords
        '''
        self.account.save_accounts()
        another_account = Records('twitter', 'User')
        another_account.save_accounts()

    def test_dislay_accounts(self):
        '''
        test method to check displaying of accounts
        '''
        self.account.save_account()
        another_account = Records("Twitter","user", "user1")
        another_account.save_account()
        self.assertEqual(Records.display_accounts(),Records.account_credentials)

    def test_search_accounts(self):
        '''
        test method to test search functionality
        '''
        self.new_account.save_account()
        another_account = Records("Twitter", "User", "123")
        another_account.save_account()
        self.assertEqual(another_account,Records.search_accounts("Twitter"))

if __name__ == "__main__":
    unittest.main()
