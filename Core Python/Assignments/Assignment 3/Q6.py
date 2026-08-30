 # write a program to calculate profit or loss.

cost_price = int(input('enter cost price:'))
selling_price = int(input('enter selling price:'))

if(selling_price > cost_price):
    profit = selling_price - cost_price
    print('profit=',profit)

elif(cost_price > selling_price):
    loss = cost_price - selling_price

else:
    print('No profit,No loss')