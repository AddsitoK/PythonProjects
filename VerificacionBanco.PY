# Yo soy slenderman y estos son mis bosques 🗣🗣
import time
locked = False
balance_old_user = 400
username_old_user = 'YoSoySlenderman'
password_old_user = 'yEstosSonMisBosques1'
age_old_user = 23
def verify_age(age):
    if age < 18:
        return True
    else:
        return False
    
registered = False
while locked == False:
    special_char = '!@#$%^&*()+{ }|:"<>?[]\\;\',./`~'
    username_new_user = input("Insert your username to register: ")
    password_new_user = input("Insert your password to register: ")
    has_eight_lenght = len(password_new_user) >= 8
    has_special_char = any(caracter in special_char for caracter in password_new_user)
    has_number = any(caracter.isdigit() for caracter in password_new_user)
    age_new_user = int(input('Insert your age to register: '))
    locked = verify_age(age_new_user)
    if locked:
        print('You are not allowed to register because you are under 18 years old.')
        time.sleep(5)
        break
    
    if age_new_user == age_old_user and username_new_user == username_old_user or password_new_user == password_old_user and username_new_user == username_old_user or age_new_user == age_old_user and password_new_user == password_old_user and username_new_user == username_old_user:
        print('You are already registered.')
    elif username_new_user == username_old_user:
        print('This username is already being used')
    elif password_new_user == password_old_user:
        print("You can't have the same password as " + username_old_user)
    elif not has_number:
        print('Your password must contain at least one number.')
    elif not has_eight_lenght:
        print('Your password must have at least 8 characters.')
    elif has_special_char:
        print('Your password must not contain special characters.')
    else: 
        print('You have successfully registered.')
        locked = True
        registered = True

while registered:
    print('Welcome to the system, ' + username_new_user + '!')
    balance_new_user = 0
    loan = 500
    time.sleep(5)
    decision = input('Do you want to take a loan of $500? (yes/no): ')
    if decision == 'yes':
        balance_new_user += loan
        print('You have successfully taken a loan of '+ str(loan) + '. Your new balance is: $' + str(balance_new_user))
    elif decision == 'no':
        print('You have chosen not to take a loan.')
    else:
        print('Invalid input. Please enter "yes" or "no".')
    decision = None
    time.sleep(5)
    decision = input('Do you want to check your balance? (yes/no): ')
    if decision == 'yes':
        print('Your current balance is: $' + str(balance_new_user))
    decision = None
    time.sleep(5)
    decision = input('Do you want to buy 400 robux? (yes/no): ')
    if decision == 'yes':
        if balance_new_user >= 400:
            balance_new_user -= 400
            print('You have successfully bought 400 robux.')
        else:
            print('You do not have enough balance to buy 400 robux.')
    elif decision == 'no':
        print('You have chosen not to buy robux.')
    else:
        print('Invalid input. Please enter "yes" or "no".')
    decision = None
    time.sleep(5)
    decision = input('Do you want to leave the system? (yes/no): ')
    if decision == 'yes':
        print('You have successfully left the system. Goodbye!')
        break
    elif decision == 'no':
        print('You have chosen to stay in the system.')
    else:
        print('Invalid input. Please enter "yes" or "no".')
    time.sleep(4)
    print('Why do you stay here?')
    time.sleep(6)
    print('Well i was about to kick you anyways.')
    time.sleep(9)
    print('You have been kicked from the system. Goodbye!')
    break