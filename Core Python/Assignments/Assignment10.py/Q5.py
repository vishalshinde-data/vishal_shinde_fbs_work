#Accept a number from user and check if this element is present in the list or not.
#Also tell how many times it is present in the list.

li = [10, 30, 20, 10, 40, 10, 50, 10]
num = int(input("Enter the number:"))
count = 0

for i in li:
    if(i == num):
        count += 1

if(count > 0):
    print("Element is present") 
    print("count =", count)
else:
    print("Element is not present")               