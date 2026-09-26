li = [50, 40, 30, 20, 10]
start = 0
end = len(li)-1
while(start < end):
    li[start], li[end] = li[end], li[start]
    
print(li)    