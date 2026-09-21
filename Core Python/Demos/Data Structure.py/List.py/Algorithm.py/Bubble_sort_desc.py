def bubblesortdesc(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size-i):
            if(li[j] < li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]

li = [40, 30, 50, 20, 10]
print(li)
bubblesortdesc(li)
print(li)