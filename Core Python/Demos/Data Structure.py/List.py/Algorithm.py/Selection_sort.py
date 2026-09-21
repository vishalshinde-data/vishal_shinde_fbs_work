def selectionsort(li):
    size = len(li)
    for i in range(0, size-1):
        max_ind = i
        for j in range(i+1, size):
            if(li[j] > li[max_ind]):
                max_ind = j
                li[i], li[max_ind] = li[max_ind], li[i]
li = [50, 40, 30, 20, 10]
print(li)
selectionsort(li)
print(li)                
