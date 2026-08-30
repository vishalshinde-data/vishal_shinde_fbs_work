#check whether a person is eligible to vote.if eligible check whether they are a first time voter.

age = int(input('enter the age:'))
first_time = input('are you first time voter? (yes/no):')

if(age >= 18):
    if(first_time == 'yes'):
        print('eligible to vote and first time voter')
    else:
        print('eligible to vote but not first time voter')    
else:
    print('not eligible to vote')        