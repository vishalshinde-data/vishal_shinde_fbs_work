def greet():
    print('good morning')

greet()  #Without function call your code will not execute.
greet()    

#addition
def addition():
    num1 = int(input('enter number 1:'))
    num2 = int(input('enter number 2:'))

    sum = num1 + num2

    print('sum:', sum)

addition()

#TYPES

#1.Without parameter Without return
def addition():
    a = 10
    b = 20
    print(a+b)
addition()

#2.Without parameter With return
def addition():
    a = 10
    b = 20
    sum = a + b
    return(sum)
result = addition()
print(result)

#3.With parameter Without return
def addition(a, b):
    print(a + b)
addition(10, 20)  

#4.With parameter With return
def addition(a, b):
    sum = a + b
    return sum
result = addition(10, 20)
print(result)