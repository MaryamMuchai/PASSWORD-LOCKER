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
		print("select the following to proceed:\n \t\t nw- To create new user use: \n \t\t ln - To login to your account use : \n \t\t dis - To Display Credentials use: \n \t\t Del -To Delete: \n \t\t ex- to Exit")
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
			while default_user_name != 'user' or default_user_password !='1234':
				print('Wrong username or password. Username "user" and password "1234"') 
				print('enter user name')
				default_user_name = input()

				print('enter password')
				default_user_password = input()
				print('\n')
			else:
				print('login success')
				print('\n')
				print('\n')
		elif short_code == 'ex':
			  break

		else:
				print('enter valid code to continue')

if __name__ == '__main__':
	main()