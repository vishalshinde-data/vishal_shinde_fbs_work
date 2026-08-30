#WAP to calculate total salary of employee based on basic , da=10% of basic,ta = 12% of basic,hra=15% basic

basic = int(input('Enter basic salary:'))

da = (10 / 100) * basic
ta = (12 / 100) * basic
hra = (15 / 100) * basic

total_salary = da + ta + hra + basic

print('DA:',da)
print('TA:',ta)
print('HRA:',hra)
print('TOTAL_SALARY:',total_salary)