# Example1

def addition(*num):
    sum = 0
    for val in num:
        sum += val
    return sum
res = addition(10, 20, 30, 40, 50)
print(res)

#Example2

def addition(*args):
    total = 0
    for val in args:
        total += val
    print('SUM:', total)
addition(10, 20)
addition(10, 20, 30, 40, 50)    