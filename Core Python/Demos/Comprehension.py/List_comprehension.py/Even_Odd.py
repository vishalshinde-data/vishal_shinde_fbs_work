#Transforming
li = [3, 9, 10, 22, 11, 7, 2, 5]
newli = []
for i in li:
    if i%2==0:
        newli.append("even")
    else:
        newli.append("odd")
print(newli)

#Comprehension
li = [3, 9, 10, 22, 11, 7, 2, 5]
newli =['even' if x%2==0 else "odd" for x in li]
print(newli)