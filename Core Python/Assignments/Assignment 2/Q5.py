#WAP to calculate selling price of book based on cost price and discount.

cp = int(input('Enter the cost price of book:'))
discount = int(input('Enter discount percentage:'))

discount_amount = (cp * discount) / 100
sp = cp - discount_amount

print('seeling price of book:', sp)