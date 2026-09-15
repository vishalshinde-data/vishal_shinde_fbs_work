#Write a program to prompt user to enter userid and password. after verifying userid and password 
#display a 4 digit random number and ask user to enter the same. if user enters the same number then
#show him success message otherwise failed.(something like captcha)
import random
userid = input('Enter the userid:')
password =input('Enter the password:')

if(userid == 'vishal' and password == '1234'):
    captch = random.randint(1000, 9999)
    print(f'your captcha={captch}')
    chuser =int(input('Enter the captcha:'))
    if(chuser == captch):
        print('user login successfully...') 
    else:
        print('Invalid captcha...')
else:
    print('User is Invalid.')               