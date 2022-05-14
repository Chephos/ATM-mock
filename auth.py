# register:
# username, email and password

# login:
# username or email and password
from multiprocessing.sharedctypes import Value
from random import randint,randrange
import database
import validation
from getpass import getpass

# database = {7097385459:['Efosa','Charles-Abu','efosacharlesabu@gmail.com','password',0]}
def init():
    '''Initialises the bank process'''
    inValidOption = True
    print('Welcome to Bank Zuri!')
    while inValidOption:
        try:
            haveAccount = int(input('Do you have an account with us? 1(yes) 2(no):\n'))
        except ValueError:
            print('Invalid input***')
            init()

        if haveAccount==1:
            inValidOption = False
            login()
            
        elif haveAccount==2:
            inValidOption = False
            register()
            
            pass
        else:
            print('Invalid Option')
    pass


def register():
    '''Registers a new user'''
    print('***** Register *****')
    email = input('Enter your email address:\n')
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    password = input('Create a password for yourself\n')
    
    accountNumber = accountNumberGenerator()

    is_user_created = database.create(accountNumber,first_name,last_name,email,password)

    # database[accountNumber] = [first_name,last_name,email,password]
    if is_user_created:
        print('Your Account has been created successfully!')
        print('== ==== == ==== ==')
        print('Your account number is %s' % (accountNumber))
        print('== ==== == ==== ==')
        
        login()
    else:
        print('Something went wrong.')
        register()
       


def login():
    '''Logs in an existing user'''

    
    accountNumberFromUser = (input('Enter your account number:\n'))
    is_account_number_valid = validation.account_number_validation(accountNumberFromUser)
    
    if is_account_number_valid:

        # passwordFromUser = input('Enter Password:\n')
        passwordFromUser = getpass('Enter Password:\n')

        user_list = database.authenticated_user(accountNumberFromUser,passwordFromUser)
        if user_list:
            bankOperation(user_list)
        else:
            print('Invalid Account number or password.')
            login()
        
        # for accountNo,userInfo in database.items():
        #     if accountNumberFromUser == str(accountNo):
        #         if passwordFromUser == userInfo[3]:
        #             bankOperation(userInfo)
        #         else:
        #             print('Invalid password, try again.')
        #             login()
                    

    
    else:
        print('Account Number Invalid: check that you have up to 10 digits and only integers')
        login()

    
def accountNumberGenerator():
    '''generates an account number'''
    
    return randrange(0000000000,9999999999)




def bankOperation(user):
    print('********************************\nWelcome %s %s' % (user[0].title(),user[1].title()))
    selectedOption = (input('These are the available options: (1) Withdrawal (2) Deposit (3) Logout (4) Exit\n'))
    try:
        int(selectedOption)
    except ValueError:
        print('Invalid Input,try again!')
        # bankOperation(user)
    else:
        if int(selectedOption)==1:
            withdrawal()
        
        elif int(selectedOption)==2:
            deposit()
            
        elif int(selectedOption)==3:
            logout()
            
        elif int(selectedOption)==4:
            exit()
            
        else:
            print('Invalid option selected.')


    
    
def withdrawal():
    pass


def deposit():
    pass

def logout():
    login()

init()

# print(accountNumberGenerator())
# print(database)