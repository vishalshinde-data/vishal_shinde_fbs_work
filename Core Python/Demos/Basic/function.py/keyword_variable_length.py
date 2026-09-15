#Example1
def emp(**data):
    for key, val in data.items():
        print(key, ':', val)
emp(id = 101, name = 'vishal', sal = 40000, dept = 'IT')        


#Example2

def student(**kwargs):
    for key, val in kwargs.items():
        print(key, ':', val)
student(name = 'vivek', age = 25, marks = 80)        
