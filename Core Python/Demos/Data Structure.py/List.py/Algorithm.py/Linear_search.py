#Take input from user
def linearsearch(li, search_ele):
    size = len(li)
    for ind in range(0, size):
        if(li[ind] == search_ele):
            return ind
    else:
        return -1

li = [10, 40, 20, 30, 50, 60]
ele = int(input("Enter the number:"))
res = linearsearch(li, ele)

if(res != -1):
    print(f"{ele} is present in index {res}.")
else:
    print(f"{ele} is not present in list.")    

#000000000000
def linearsearch(li, search_ele):
    size = len(li)
    for i in range(0, size):
        if(li[i] == search_ele):
            return i
    else:
        return -1

li = [10, 30, 40, 20, 60, 50]
ele = 20
res = linearsearch(li, ele)

if(res != -1):
    print(f"{ele} is present in index {res}.")
else:
    print(f"{ele} is not present in list")    

