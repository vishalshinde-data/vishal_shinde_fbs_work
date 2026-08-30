#login system using nested if.

username = input('enter username:')
password = input('enter password:')

if(username == 'vishal'):
    if(password == '1234'):
        print('login successful.')
    else:
        print('Incorrect password')
else:
    print('Incorrect username')            