# Zuri Python Mock ATM

name = input('Enter your name:\n').title()
allowedUsers = ['Precious','Kunle','Efosa','Chioma']
allowedPasswords = ['passwordPrecious','passwordKunle','passwordEfosa','passwordChioma']
availableBalance = {'Precious':500_000,'Kunle':50_000,'Efosa':200_000_000,'Chioma':100_000_000}

if name in allowedUsers:
    userId = allowedUsers.index(name)
    password = input('Password:\n')

    if password == allowedPasswords[userId]:
        print(f'\nWelcome {name}')
        print(f'\nThese are the options available:')
        print('1. Withdrawal\n2. Cash Deposit\n3. Complaint')

        selectedOption = int(input('\n>> '))
        
        if selectedOption == 1:
            # Withdrawal
            withdrawalAmount = int(input('Enter amount you want to withdraw:\n'))
           # print(">> 10000\n>>5000\n>>3000>>\n2000>>\n1000")
            if withdrawalAmount<= (availableBalance[name] - 1000):
                availableBalance[name] -=withdrawalAmount
                print('Withdrawal successful!')
            else:
                print('Insufficient funds')

            
        elif selectedOption == 2:
            # cash deposit
            print('Amount to deposit:')
            depositAmount = int(input())
            availableBalance[name]+=depositAmount
            print(f'Deposit successfull, your available balance is {availableBalance[name]}')



            pass
        elif selectedOption == 3:
            # Complaint
            complaint = input('\nWe apologise for any inconviniences, kindly fill in your complaints here:\n')
            print('Your complaints have been saved and we will get back to you shortly, thank you.')

            
        else:
            print('Option not available.')

    else:
        print('Incorrect Password, try again.')

else:
    print('Invalid user, try again.')
