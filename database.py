# CRUD operations
# create record
# read record
# update record
# delete record
import os

user_db_path = 'data/user_record'

def create(user_account_number,first_name,last_name,email,password):
    # create a file with account_number.txt as name of file
    if does_account_number_exist(user_account_number):
        return False
        
    user_details = f'{first_name},{last_name},{email},{password},{0}'

    if does_email_exist(email):
        print('Email already in use')
        return False

    completion_state = False

    try:
        f = open(f'{user_db_path}/{user_account_number}.txt','x')
        
    except FileExistsError:
        # delete already created file, and print out error then return false
        does_file_contain_data = read(user_account_number)
        if not does_file_contain_data:
            delete(user_account_number)
        
        # check content of file before deleting  
    else:
        f.write(str(user_details))
        completion_state=True
    finally:
        f.close()# Error here
        return completion_state

    # writes user details into the file and save
    # if saving to a file fails, then delete created file
    


def read(user_account_number):
    # find user with account number
    user = find(user_account_number)
    if user is not None:
        try:
            f = open(f'{user_db_path}/{user}')
        except FileNotFoundError:
            print('User not found!')
        except FileExistsError:
            print('User does not exist')
        except TypeError:
            print('Invalid account number format')
        else:
            user_data = f.readline()
            f.close()
        
        return user_data
    else:
        print("User does not exist")
        return False

    # fetch content of file
    

def update(user_account_number):
    #find user with account number
    # fetch content of file
    # write to file
    # save file 
    pass

def delete(user_account_number):
    # fetch users account to be deleted
    is_delete_successful = False
    if os.path.exists(f"{user_db_path}/{user_account_number}.txt"):
        try:
            os.remove(f'{user_db_path}/{user_account_number}.txt')
        except FileNotFoundError:
            print('User not found')
        else:
            is_delete_successful=True
    # delete file
        finally:
            return is_delete_successful
    pass

def find(user_account_number):
    all_users =  os.listdir(user_db_path)
    for user in all_users:
        if user.endswith(f'{user_account_number}.txt'):
            return user

    return None
    
    pass

def does_email_exist(email):

    all_users = os.listdir(user_db_path)
    for user in all_users:
        with open(f'{user_db_path}/{user}','r') as f:
            user_list = ((f.readline()).split(','))
            if email in user_list:
                return True
    return False
        # print(user)


def does_account_number_exist(user_account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == f'{user_account_number}.txt':

            return True
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        # user_raw = read(account_number)
        with open(f'{user_db_path}/{account_number}.txt','r') as f:
            user_list = ((f.readline()).split(','))
            if password == user_list[-2]:
               return user_list
            else:
                return False
    else:
        return False
    
# create(7097385459,['Efosa','Charles-Abu','efosacharlesabu@gmail.com','password',0])
# delete(622507728)

# print(read(6634087857))
# does_email_exist('efosacharlesabu@gmail.com')
# print(does_account_number_exist(1810031990))