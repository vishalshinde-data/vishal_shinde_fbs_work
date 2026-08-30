#check whether the character is uppercase,lowercase,digit or special character.
ch = input('enter the character:')

if(ch >= 'A' and ch <= 'Z'):
    print('character is in uppercase')

elif(ch >= 'a' and ch <= 'z'):
    print('character is in lowercase')

elif(ch >= '0' and ch <= '9'):
    print('character is a digit')

else:
    print('it is a special character')
