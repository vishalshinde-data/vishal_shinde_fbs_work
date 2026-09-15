# largest numbers than 20
numbers  = [10, 20, 30, 45, 85, 8, 3, 79, 23, 45, 84, 87]
greater = list(filter(lambda x: x >= 20, numbers))

print(greater)

#smallest numbers than 20
numbers = [1, 3, 14, 70, 57, 43, 19, 20, 15, 9, 10]
smallest = list(filter(lambda x: x <= 20, numbers))

print(smallest)