#WAP to print all numbers in a range divisible by a given number.
start = int(input('enter starting number:'))
end = int(input('enter ending number:'))
n = int(input('enter the number:'))

for i in range(start, end+1):
    if(i % n == 0):
        print(i)
