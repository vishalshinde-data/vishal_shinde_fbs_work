#Write a program to remove duplicates from the list.

li = [10, 20, 10, 30, 40 ]
duplicate = 0

for i in li:
    if i not in duplicate:
        duplicate.append(i)

print(duplicate)        
