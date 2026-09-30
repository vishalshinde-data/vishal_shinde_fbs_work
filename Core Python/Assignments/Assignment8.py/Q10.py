#write a program to check if entered year is leap year or not.

def leapyear(year):
    if(year % 400 == 0):
        print("leap year")
    elif(year % 100 == 0):
        print("not leap year")
    elif(year % 4 == 0):
        print("leap year")    
    else:
        print("not leap year")

year = int(input("enter the leap year:"))
leapyear(year)