#input 5 subject marks from user and display grade (e.g. first class,second class)

m1 = int(input('enter first subject mark:'))
m2 = int(input('enter second subject mark:'))
m3 = int(input('enter third subject mark:'))
m4 = int(input('enter fourth subject mark:'))
m5 = int(input('enter fifth subject mark:'))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print('Total:',total)
print('Percentage',percentage)

if(percentage >= 90):
    print('Grade A')
elif(percentage >= 80):
    print('Grade B')
elif(percentage >= 70):
    print('Grade c')
elif(percentage >= 60):
    print('Grade D')
else:
    print('Grade E')                