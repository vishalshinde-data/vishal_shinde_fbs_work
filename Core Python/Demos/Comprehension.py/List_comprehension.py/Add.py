li = [10, 1, 20, 11, 13, 14]
newlist = []
for i in li:
    newlist.append(i + 10)
print(newlist)   


#Comprehension
li = [10, 1, 20, 11, 13, 14]
newlist = [i + 10 for i in li]
print(newlist)
