#income tax calculation.

income = int(input('enter the annual income:'))

if(income <= 25000):
    tax = 0

elif(income <= 50000):
    tax = income * 0.05

elif(income <= 100000):
    tax = income * 0.20

else:
    tax = income * 0.30

print('Income tax:',tax)    