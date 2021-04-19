import unittest
from user import User
from user import Records

class UserTest(unittest.TestCase):
    
    '''
    test class that defines test cases for the user class
    '''
    def setUp(self):
        self.new_user = User('User','0123')

    def test_init(self):
        '''
        test case to check if its initialized properly
        '''
        self.assertEqual(self.new_user.username,'User')
        self.assertEqual(self.new_user.password,'0123')
    
    def test_save_user(self):
        '''
        test case to test if new user instance has been saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestRecords(unittest.TestCase):
    '''
    test class that defines test cases for the Records class
    '''
    def setUp(self):
        self.new_record = Records('Gmail','user', '0123')
    def test_init(self):
        '''
        test case to check if instance is initalized correctly
        '''
        self.assertEqual(self.new_record.account,'Gmail')
        self.assertEqual(self.new_record.userName,'user')
        self.assertEqual(self.new_record.password,'0123')

    def save_record_test(self):
        '''
        test case to test if the object is saved
        '''
        self.new_record.save_details()
        self.assertEqual(len(Records.records_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has been run
        '''
        Records.records_list = []

    def test_save_many_accounts(self):
        self.new_record.save_details()
        test_record = Records("fb","user","0123")
        test_record.save_details()
        self.assertEqual(len(Records.records_list),2)

    def test_delete_record(self):
        '''
        test case for the delete function
        '''
        self.new_record.save_details()
        test_record = Records('fb','user','0123')
        test_record.save_details()

        self.new_record.delete_record()
        self.assertEqual(len(Records.records_list),1)

    def test_find_records(self):
        '''
        test case to check if account can be searched
        '''
        self.new_record.save_details()
        test_record = Records('fb','user','0123')
        test_record.save_details()

        the_record = Records.find_record('fb')

        self.assertEqual(the_record.account,test_record.account)

    def test_display_all_records(self):
        '''
        test case that displays all saved records
        '''
        self.assertEqual(Records.display_records(),Records.records_list)




    
if __name__ == "__main__":
    unittest.main()
