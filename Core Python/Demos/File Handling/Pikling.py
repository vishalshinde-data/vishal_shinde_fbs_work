# class Student:
#     def __init__(self,rno,name,marks):
#         self.rollno=rno
#         self.name=name
#         self.marks=marks
#     def selfname(self,newname):
#         self.name=newname  
#     def getname(self):
#         return self.name
#     def __str__(self):
#         return f"{self.rollno}{self.name}{self.marks}"
# s1=Student(12,"vishal",67) 

# # with open("abcde.txt",'w') as f:

# with open("abcde.txt","r")as f:
#     d=f.read()
#     print(d)
#     #d.setname("virat")
#     dlist=d.split()
#     print(dlist)
#     id=int(dlist[0])
#     name=(dlist[1])
#     marks=(dlist[2])
#     e1=Student(id,name,marks)
#     e1.setname("ram")
#     print(e1)




# with open("abc.txt","r+")as f:
#     f.write("MI")
#     d=f.read()
#     f.write("KKR")
#     print(d)



# with open("abc.txt","w+")as f:
#     f.write("RCB won the 2 cups")
#     print(f.tell())
#     f.seek(0)
#     d=f.read()
#     print(d)



# with open("abc.txt",'a+')as f:
#     print(f.tell())
#     f.seek(19)
#     d=f.readlines()
#     print(d)
#     print(f.tell())



                                