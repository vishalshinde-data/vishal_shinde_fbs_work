#Write a program to calculate the percentage of student based on marks of any five subjects.

m1 = int(input('enter marks of subject 1:'))
m2 = int(input('enter marks of subject 2:'))
m3 = int(input('enter marks of subject 3:'))
m4 = int(input('enter marks of subject 4:'))
m5 = int(input('enter marks of subject 5:'))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500)  * 100

print('total marks:', total)
print('percentage:', percentage)