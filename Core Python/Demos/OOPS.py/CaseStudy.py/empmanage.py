from hr import HR
from dev import Devloper
class Empmanage:
    empDetail={}
    def addEmp(self):
        emp=None
        eid=int(input("Enter the Id of Emp="))
        if eid in Empmanage.empDetail:
            print("Employee with this id is allready exist")
        else:
            ename=input("Enter the Name=")
            sal=float(input("Enter the Salary="))
            print("1.HR\n2.Developer")
            chio=int(input("Enter the choice="))  
            if chio==1:
                com=float(input("Enter the commition of Hr"))
                emp=Hr(eid,ename,sal,com)
            elif chio==2:
                bonus=float(input("Enter the bonus of Dev"))   
                emp=Developer(eid,ename,sal,bonus) 
            else:
                print("Invalid choice")
                return  
            Empmanage.empDetails[eid]= emp   
        print("I am in Add Emp")
    def displayEmp(self):
        print("I am in Display Emp")
    def updateEmp(self):
        print("I am in Update Emp")
    def searchEmp(self):
        print("I am in Search Emp")
    def deleteEmp(self):
        print("I am in Delete Emp")
    
    