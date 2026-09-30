#WAP to check if agiven number armstrong number or not. For each 
#task create separete function.

def armstrong(num):
    temp = num
    sum = 0

    while(num > 0):
        digit = num % 10
        num = num // 10
        sum = sum + digit ** 3

    if(sum == temp):
        print("armstong number")
    else:
        print("not armstrong number")        

num = int(input("enter the armstrong number:"))
armstrong(num)