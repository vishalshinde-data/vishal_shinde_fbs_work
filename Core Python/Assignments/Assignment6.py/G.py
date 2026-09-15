for i in range(1, 6 ):
    for j in range(1, 6-i ):
        print(' ', end = ' ')    

    for j in range(i * 2-1 ):
        print(chr(65+j), end = ' ')
    print()        