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
        account_records=[] #showing the list of all account

def __init__(self, account_name, user_name, password):

        '''
        initialization of the account object
        '''

        self.new_account=new_user
        self.user_name = Username
        self.password = password if password else Records.password_generate()

def save_accounts(self):
    '''
    method to save account object
    '''
    Records.account_records.append(self)

def delete_accounts(self):
    '''
    method to delete an account
    '''
    Records.account_records.remove(self)

@classmethod
def display_account(cls):
    '''
    class method that displays all given accounts
    '''
    return cls.account_records

@classmethod
def search_accounts(cls, search):
    '''
    class method that searchs an account
    '''


