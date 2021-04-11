import random
from user import User , Records



def create_user(username, password):
    '''
    function to create a new user
    '''
    user = User(username, password)
    return user


def save_user(user):
    '''
    function to save a new user
    '''
    user.save_user()


def create_account(account, user, password):
    '''
    function to a new a/c
    '''
    new_record = Records(account, user, password)
    return new_record


def save_accounts(records):
    '''
    function to save the new a/c
    '''
    records.save_accounts()


def delete_records(records):
    '''
    function to deleting an a/c
    '''
    records.delete_records()


def search_accounts(search):
    '''
    function to find a/c name
    '''
    return Records.search_accounts(search)


def generate_password():
	'''
    generating password
    '''
	auto_password=Records.generatePassword()
	return auto_password

def copy_password(acc):
	return Records.copy_password(acc)


def display_accounts_details():
    '''
    function to display all accounts
    '''
    return Records.display_records()

def login_user(username,password):
	'''
	checks for user and logs in
	'''

	check_user = Records.verify_user(username,password)
	return check_user

def check_records(account):
	'''
	creates new records
	'''
	return Records.if_records_exist(acc)

def find_record(acc):
	return Records.find_records(acc)


def main():
	while True:
		print("Welcome to password locker !!!")
		print('\n')
		print("select the following to proceed:\n \t\t nw-To create new user \n \t\t ln-To login to your account \n \t\t dis-To Display Credentials \n \t\t del-To Delete: \n \t\t ex- to Exit")
		short_code = input().lower()
		print('\n')
		if short_code == 'nw':
			print('create username')
			created_user_name = input()
			while True:
				print(" TP - To type your own pasword:\n GP - To generate random Password")
				password_Choice = input().lower().strip()
				if password_Choice == 'tp':
					password = input("Enter Password\n")
					break
				elif password_Choice == 'gp':
					password = generate_Password()
					break
				else:
					print("Invalid password please try again")
			save_user(create_user(username,password))
			print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
			
		elif short_code == 'ln':
			print('welcome')
			print('enter user name')
			default_user_name = input()
			print('enter password')
			default_user_password = input()
			print('\n')
			while default_user_name != 'user' or default_user_password != '0123':
				print("Wrong username or password. Username 'user' and password '0123'")
				print('enter user name')
				default_user_name = input()
				print('enter password')
				default_user_password = input()
				print('\n')
			else:
				print('login success')
				print("Hello %s Welcome to the locker manager"%(created_user_name))
				print('\n')	
		elif short_code == 'dis':
			if display_acc():
				print('Here is a list of all yor accounts:\n')
				for account in display_acc():
					print(f" Acc:{acc.acc} \n User Name:{created_user_name}\n Password:{created_user_password}")
			else:
				print('\n')
				print('you dont have any saved accounts')
		elif short_code == "fa":
			print("Enter the name of the account you want to serach for")
			search_acc = input().lower
			if find_records(search_acc):
				search_acc = find_records(search_accounts)
				print(f"Account Name : {search_acc}")
				print(f"User Name: {search_acc.user_name} password:{search_acc.password}")
			else:
				print("That Credential does not exist")
				print('\n')
		elif short_code == 'del':
			print('\n')
			print('Enter the account name you want to delete eg:Twitter')
			search_accounts = input().lower()
			if find_acc(search_acc):
				search_acc.delete_accounts()
				print('\n')
				print("The account: {search_acc.acc} has been deleted")
				print('\n')
			else:
				print("There is no record of the item you are trying to delete")
				
		elif short_code == 'ex':
			print('\n')
			print(f"Have a lovely day, {user_name}")
			break
		
		else:
			print('enter valid code to continue')


if __name__ == '__main__':
    main()
