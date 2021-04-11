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
