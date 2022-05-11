# register:
# username, email and password

# login:
# username or email and password
from random import randint,randrange

database = {}
def init():
    '''Initialises the bank process'''
    inValidOption = True
    print('Welcome to Bank Zuri!')
    while inValidOption:
        haveAccount = int(input('Do you have an account with us? 1(yes) 2(no):\n'))

        if haveAccount==1:
            inValidOption = False
            login()
            pass
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

    database[accountNumber] = [first_name,last_name,email,password]
    print('Your Account has been created successfully!')
    print('== ==== == ==== ==')
    print('Your account number is %s' % (accountNumber))
    print('== ==== == ==== ==')
    
    login()


def login():
    '''Logs in an existing user'''

    
    accountNumberFromUser = int(input('Enter your account number:\n'))
    passwordFromUser = input('Enter Password:\n')
    for accountNo,userInfo in database.items():
        if accountNumberFromUser == accountNo:
            if passwordFromUser == userInfo[3]:
                bankOperation(userInfo)

    print('Invalid account number or password,try again.')
    
        

    


def accountNumberGenerator():
    '''generates an account number'''
    # numbers = [for i in range(1,10)]
    # accountNumber = ''
    # for i in range(10):
    #     accountDigit = str(randint(0,10))
    #     accountNumber += accountDigit

    # database['fullname']= accountNumber
    
    return randrange(0000000000,9999999999)


def bankOperation(user):
    print('Welcome %s %s' % (user[0].title(),user[1].title()))
    selectedOption = int(input('These are the available options: (1) Withdrawal (2) Deposit (3) Logout (4) Exit\n'))

    if selectedOption==1:
        withdrawal()
    
    elif selectedOption==2:
        deposit()
        
    elif selectedOption==3:
        logout()
        
    elif selectedOption==4:
        exit()
        
    else:
        print('Invalid option selected.')


    pass
    
def withdrawal():
    pass


def deposit():
    pass

def logout():
    login()

init()

# print(accountNumberGenerator())
# print(database)