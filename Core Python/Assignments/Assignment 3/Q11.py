total = 0
age = int(input('Enter the age:'))
ticket = int(input('Enter the amount:'))

for i in range(1, 6):
    if(age <= 12):
        ticket = ticket - (ticket * 30 / 100)
    elif(age > 59):
        ticket = ticket - (ticket * 50 / 100)
    else:
        ticket = ticket

    total = total + ticket
print('Total ticket amount:', total)            

