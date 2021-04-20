import random
import string
import pyperclip
class User:
    """
    Create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        deletes a  saved account from the list
        '''
        User.user_list.remove(self)

class Records():
    """
    Create records class to help create new objects
    """
    records_list = []
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        method that defines user records to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store a new list
        """
        Records.records_list.append(self)

    def delete_record(self):
        """
        delete_record method that deletes an account credentials 
        """
        Records.records_list.remove(self)
    
    @classmethod
    def find_record(cls, account):
        """
        Method that takes in a account_name and returns a record that matches that account_name.

        """
        for record in cls.records_list:
            if record.account == account:
                return record
    @classmethod
    def copy_password(cls,account):
        found_records = Records.find_records(account)
        pyperclip.copy(found_records.password)

    @classmethod
    def if_records_exist(cls, account):
     
        for records in cls.record_list:
            if records.account == account:
                return True
        return False
    @classmethod
    def display_records(cls):
        """
        Method that returns all the list in the record

        """
        return cls.records_list

    def generate_password(stringLength=8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
        
        