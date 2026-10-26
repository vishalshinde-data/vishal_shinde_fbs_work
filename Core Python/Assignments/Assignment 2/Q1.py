# Convert the time entered in hh,min and sec into seconds.

Hour = int(input("Enter the hour:"))
Minute = int(input("Enter the minute:"))
Second = int(input("Enter the second:"))

Total_second = (Hour * 3600) + (Minute * 60) + Second

print("Total number of second:", Total_second)


