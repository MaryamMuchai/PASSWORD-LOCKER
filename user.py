import random
import pyperclip

class User:

    '''
    class that generate new instance of the user
    '''

    user_list = []

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        save_user method saves a new user objects to the user_list
        '''

        User.user_list.append(self)

class Records:
    '''
    class that creates new account credentials
    '''
    account_records=[] #showing the list of all accounts

    def__init__(self, account_name, user_name, password = None):
    '''
    initialization of the account object
    '''
    self.account_name = account_name
    self.user_name = Username
    self.password = password if password else Records.password_generate()


