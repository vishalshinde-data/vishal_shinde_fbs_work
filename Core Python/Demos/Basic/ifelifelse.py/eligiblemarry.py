#eligible or not eligible for marriage.
gender = input('Enter gender (m/f):')
age = int(input('Enter age:'))

if(gender == 'f'):
    if(age >= 18):
        print('girl is eligible for marriage.')
    else:
        print('pehle padhai kar lo.') 
else:
    if(age >= 21):
        print('boy is eligible for marriage.')           
    else:
        print(' pehle kama lo.')       