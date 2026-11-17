li = [3, 9, 10, 22, 11, 7, 2, 5]
newLi = []
for i in li:
    if i % 2 != 0:
        newLi.append(i * i)
print(newLi)        



#comprehension
li = [3, 9, 10, 22, 11, 7, 2, 5]
newLi = [x * x for x in li if x % 2 != 0]
print(newLi)
