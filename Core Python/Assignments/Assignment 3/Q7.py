#write a program to check if user has entered correct user id and password

userid = input('enter userid:')
password = input('enter password:')

if(userid == 'vishal'):
    if(password == '1234'):
        print('login successfully')
    else:
        print('Incorrect password')
else:
    print('Incorrect user id')            