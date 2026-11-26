f = open("abc.txt", 'r')
d =f.read()
print(d)

print(type(d))
f.close()
print(f.readlines())