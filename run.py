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
		print("Welcome to password locker!!!")
		print('\n')
		print("select the following to proceed:\n \t\t nw-To create new user \n \t\t ln-To login to your account \n \t\t dis-To Display Credentials \n \t\t del-To Delete: \n \t\t ex- to Exit")
		short_code = input().lower()
		print('\n')

		if short_code =='nw':
			print('create username')
			created_user_name = input()

			print('create password')
			created_user_name = input()

			print('Confirm password')
			confirm_password = input()

			while confirm_password != created_user_name:
				print('password did not match!')
				print('enter your password')
				created_user_name = input()
				print('confirm password')
				confirm_password = input()
			else:
				print(f'congratulations{created_user_name}! account creation successful')
				print('\n')
				print('proceed to login')
				print('Username')
				entered_username = input()
				print('your password')
				entered_password = input()

			while entered_username != created_user_name or entered_password != created_user_password:
				print('Invalid username or password')
				print('Username')
				entered_username = input()
				print("Your password")
				entered_password = input()

			else:
				print('welcome: {entered_user_name} to your account')
				print('\n')

		
		elif short_code == 'ln':
			print('welcome')
			print('enter user name')
			default_user_name = input()


			print('enter password')
			default_user_password = input()
			print('\n')
			while default_user_name != 'user' or default_user_password !='0123':
				print("Wrong username or password. Username 'user' and password '0123'") 
				print('enter user name')
				default_user_name = input()

				print('enter password')
				default_user_password = input()
				print('\n')
			else:
				print('login success')
				print('\n')
				print('\n')

        elif short_code == 'dis':
            if display_account() !=[]:
                print('\n')
                print('Here is a list of all yor accounts:\n')
                for item in display_account():
                    print(item.account_name+"\t -->"+ item.user_name +"\t-->"+item.user_password)
            else:
                print('\n')
                print('you dont have any saved accounts')

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