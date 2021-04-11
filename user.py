import random
import pyperclip

class User:

    '''
    class that generate new instance of the user
    '''

    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves a new user objects to the user_list
        '''
        User.user_list.append(self)


def __init__(self, account_name, user_name, password):

        '''
        initialization of the account object
        '''

        self.new_account=new_user
        self.user_name = Username
        self.password = password if password else Records.password_generate()

def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password
        
        def save_user(self):
            
            '''
            A method that saves a new user instace into the user list
            '''

        User.user_list.append(self)
        
        @classmethod
        def display_user(cls):
            return cls.user_list
            
            def delete_user(self):
                
                '''
                delete_account method deletes a  saved account from the list
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
        method that defines user store records
        """
        self.account = account
        self.username = username
        self.password = password
    
    def save_details(self):
        """
        method to store a new records
        """
        Records.recordss_list.append(self)

    def delete_records(self):
        """
        delete accounts
        """
        Records.records_list.remove(self)
    
    @classmethod
    def find_records(cls, account):
        """
        Method that takes in a account name and returns a record that matches.

        """
        for records in cls.records_list:
            if records.account == account:
                return records
    @classmethod
    def copy_password(cls,account):
        found_records = Records.find_records(account)
        pyperclip.copy(found_records.password)

    @classmethod
    def if_records_exist(cls, account):
        for records in cls.records_list:
            if records.account == account:
                return True
        return False
    @classmethod
    def display_records(cls):
        """
        Method that returns all items in the record 

        """
        return cls.records_list

    def generatePassword(stringLength=8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))