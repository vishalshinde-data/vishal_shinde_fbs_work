#1. Append()
a = [10, 20, 30, 40, 50, 60, 70, 80]
a. append(90)
print(a)

#2. Insert()
a = [10, 20, 30, 50, 60, 70, 80]
a . insert(3, 40)
print(a)

#3.Extend()
a = [10, 20, 30]
b = [40, 50, 60]
a. extend(b)
print(a)

#4.Remove()
a = [10, 20, 30, 40, 50, 60, 70, 80]
a. remove(30)
print(a)

#5.Pop()
a = [10, 20, 30, 40, 50, 60, 70, 80]
a. pop(2)
print(a)

#6.Clear()
a = [10, 20, 30, 40, 50, 60, 70, 80]
a. clear()
print(a)

#7.Sort() Ascending
a = [20, 40, 10, 50, 70, 30, 60]
a. sort()
print(a)

#Descending
a = [20, 40, 10, 50, 70, 30, 60]
a. sort(reverse = True)
print(a)

#8.Reverse()
a = [60, 40, 30, 20, 10, 50, 80, 70]
a. reverse()
print(a)

#9.Count()
a = [10, 20, 30, 10, 50, 10, 70, 80]
print(a. count(10))

#10.Index()
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a. index(30))

#11.copy()
a = [10, 20, 30, 40, 50, 60, 70, 80]
b = a. copy()
print(b)

#12. slice()
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[1:5])

#13.length()
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(len(a))

#extra
#Min and Max
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(min(a))
print(max(a))


