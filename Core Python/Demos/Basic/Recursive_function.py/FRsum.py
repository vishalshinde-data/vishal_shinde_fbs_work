def sumofseries(n):
    if(n <= 0):
        return 0 
    else:
        return n + sumofseries(n-1)
n = int(input("enter the number:"))
res = sumofseries(n)
print(res)    