#write a program to check if person is eligible to marry or not (maleage>=21 and female>=18)

gender = input('enter the gender(m/f):')
age = int(input('enter the age:'))

if(gender == 'f'):
    if(age >= 18):
        print('Girl is eligible for marry.')
    else:
        print('pehle padhai kar loo')    
else:
    if(age >= 21):
        print('Boy is eligible for marry.')
    else:
        print('Pehle kama loo')            