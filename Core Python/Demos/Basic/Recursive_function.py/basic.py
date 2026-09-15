def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
n = 5
show(n)    


def show(n):
    if(n == 11):
        return
    print(n)
    show(n+1)
n = 1
show(n)    

