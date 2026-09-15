#3. Example3
def emp(id, name, sal, dept = 'backoffice'):
    print('ID:', id)
    print('NAME:', name)
    print('SALARY:', sal)
    print('DEPARTMENT:', dept)

emp(101, 'vishal', 4000, 'sales')    
emp(102, 'ram', 4000, )    


#2. Example2
def greet(name = 'ram'):
    print('Hello', name)
greet('vishal')
greet()    

