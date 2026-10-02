#write a program to create a new list from existing list 
#which contain cube of each number of list.

def cube_list(li):
    new_list = []
    for i in li:
        new_list = new_list + [i ** 3]

    return new_list

li = [1, 2, 3, 4, 5]
result = cube_list(li)
print(result)    
    