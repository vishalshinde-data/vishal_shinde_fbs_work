def selectionsortdesc(li):
    size = len(li)
    for i in range(0, size-1):
        min_ind = i
        for j in range(i+1, size):
            if(li[j] > li[min_ind]):
                min_ind = j
                li[i], li[min_ind] = li[min_ind], li[i]

li = [20, 30, 50, 10, 40]
print(li)
selectionsortdesc(li)
print(li)


