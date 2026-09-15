# Write a program to prompt user to enter userid and password. if id and password is incorrect
# give him chance to re-enter the credentials. Let him try 3 times.after that program to terminate

correct_id = 'admin'
correct_password = '1234'

for i in range(3):
    userid = input('Enter userid:')
    password = input('Enter password:')

    if(userid == correct_id and password == correct_password):
        print('login successfully')
        break
    else:
        print('Incorrect userid or password')
else:
    print('you have exceeded 3 attemps. program terminated.')        