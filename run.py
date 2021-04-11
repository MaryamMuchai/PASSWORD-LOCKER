import random
from user import User


def create_user(user, password):
    '''
    function to create a new user
    '''
    new_user = User(user, password)
    return new_user


def save_user(data):
    '''
    function to save a new user
    '''
    data.save_user()


def create_account(account, user, password):
    '''
    function to a new a/c
    '''
    new_account = Records(account, user, password)
    return new_account


def save_accounts(records):
    '''
    function to save the new a/c
    '''
    records.save_accounts()


def delete_accounts(records):
    '''
    function to deleting an a/c
    '''
    records.delete_accounts()


def search_accounts(search):
    '''
    function to find a/c name
    '''
    return Records.search_accounts(search)


def generate_password():
    '''
    generating password
    '''
    random_password = Record.password_generate()
    return random_password


def display_account():
    '''
    function to display all accounts
    '''
    return records.display_account()


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
			    print("\n \t\t tp- To type your own password \n \t\t gp- To generate random password")
			    password_choice = input().lower()
			    if password_choice == 'tp':
				    password = input("Enter your password\n")
				    break
				
		elif short_code == 'gp':
				password = generate_password()
				break
			
		#else:
				#print("invalid password please try again")
				#save_user(create_user(username,password))
				#print(f"Hello {created_user_name}, You have successfully created an account. You password is: {created_user_password}")
		
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
				print(f"Hello {created_user_name}Welcome to the locker manager")
				print('\n')	
		elif short_code == 'dis':
			if display_account() != []:
				print('Here is a list of all yor accounts:\n')
				for account in display_account():
					print(f" Account:{account.account} \n User Name:{created_user_name}\n Password:{created_user_password}")
			else:
				print('\n')
				print('you dont have any saved accounts')
		elif short_code == "fa":
			print("Enter the name of the account you want to serach for")
			search_accounts = input().lower
			if find_records(search_accounts):
				search_accounts = find_records(search_accounts)
				print(f"Account Name : {search_accounts}")
				print(f"User Name: {search_accounts.user_name} password:{search_accounts.password}")
			else:
				print("That Credential does not exist")
				print('\n')
		elif short_code == 'del':
			print('\n')
			print('Enter the account name you want to delete eg:Twitter')
			item = input()
			if search_accounts(item):
				delete_accounts(search_accounts(item))
				print('\n')
				print("The account has been deleted")
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
