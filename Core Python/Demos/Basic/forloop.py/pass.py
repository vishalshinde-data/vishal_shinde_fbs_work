#pass: neglect expected indentation error.
for i in range(1,10):
    pass

#break: for terminating the loop
for i in range (1,10):
    if(i == 4):
        break      #else block will not execute in break statement.
    print(i)

#continue: to stop particular iteration
for i in range(1,10):
    if(i == 4):
        continue
    print(i)
#else: will execute when loop executed successfully.
for i in range(1,10):
    if(i == 4):
        continue
    print(i)
else:
    print('Else block execute')    