#create a simple atm program using nested if.

balance = int(input('enter your balance:'))
pin = int(input('enter PIN:'))

if(pin == 1234):
    print('PIN is correct')

    amount = int(input('enter your widrawal amount:'))

    if(amount <= balance):
        print('please collect your amount')

        balance = balance - amount
        print('remaning balance:',balance)
    else:
        print('insufficient balance')
else:
    print('Incorrect PIN')                
