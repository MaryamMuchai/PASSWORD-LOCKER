#!/usr/bin/env python3.8
import random
from user import User , Records

 
def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Records.verify_user(username,password)
    return check_user

def create_new_record(account,userName,password):
    """
    Function that creates new records for a given user account
    """
    new_record = Records(account,userName,password)
    return new_record
def save_record(record):
    """
    Function to save records
    """
    record. save_details()
def display_accounts_details():
    """
    Function that returns all the saved accounts
    """
    return Records.display_records()

def delete_record(records):
    """
    Function to delete the records in the list
    """
    record.delete_record()

def find_record(account):
  
    return Records.find_record(account)
def check_records(account):
    
    return Records.if_record_exist(account)

def generate_password():
    '''
    generates a random password for the user.
    '''
    auto_password=Records.generate_password()
    return auto_password

def copy_password(account):

    return Records.copy_password(account)
    
    
def main():
    print('\n')
    print("Welcome to password locker!!!")
    print("Select the following to proceed: \n \t\t CA-Create New Account  \n \t\t LI-Login to your account")
    short_code=input("").lower().strip()
    
    if short_code == "ca":
        username = input("User_name: ")
        while True:
            print(" \n\t\t TP-To type your own pasword: \n\t\t GP-To generate random Password")
            password_Choice = input()
            if password_Choice =='tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print(f"Hello {username}, Your account has been logged in succesfully! Your password is: {password}")
                
    elif short_code == "li":
        print("Enter your User name and your Password to log in:")
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord-Locker")  
            print('\n')
    while True:
        print("choose the following short code: \n\t\t nw- Create Account \n\t\t display- Display Credentials \n\t\t find - Find a credential \n\t\t del - Delete credential \n\t\t ex - Exit the application ")
        short_code = input().lower().strip()
        if short_code == "nw":
            print("Account name")
            account = input().lower()
            print("Your Account username")
            userName = input()
            
            while True:
                print(" \n\t\t TP - To type your own pasword if you already have an account:")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_record(create_new_record(account,userName,password))
            print('\n')
            print(f"Account record for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == 'display':
            if display_accounts_details():
                print("Here's your list of accounts: ")
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
            else:
                print("Sorry we cant find what you are looking for")
                
        elif short_code == "find":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_record(search_name):
                search_record = find_record(search_name)
                print(f"Account Name : {search_record.account}")
                print(f"User Name: {search_record.userName} Password :{search_record.password}")
                
            else:
                print("Sorry we cant find what you are looking for")
                print('\n')
                
        elif short_code == "del":
            print("Enter the account name  you want to delete")
            search_name = input().lower()
            
            if find_record(search_name):
                search_record = find_record(search_name)
                search_record.delete_record()
                print('\n')
                print(f"Your stored accounts for : {search_record.account} successfully deleted!!!")
                print('\n')
                
            else:
                print("sorry can't find the account you are looking for, kindly check again")
                
        elif short_code == 'gp':
            password = generate_Password()
            print(f" {password} You can proceed to use it to your account")
        elif short_code == 'ex':
            print("See you next time!")


if __name__ == '__main__':
    main()
