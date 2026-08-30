#calculate discount based on purchase amount.

amount = int(input('enter purchase amount:'))

if(amount <= 5000):
    discount = 0

elif(amount <= 10000):
    discount = amount * 0.10

elif(amount <= 20000):
    discount = amount * 0.20

else:
    discount = amount * 0.30

final_amount = amount - discount

print('Discount:',discount)
print('Final_amount:',final_amount)