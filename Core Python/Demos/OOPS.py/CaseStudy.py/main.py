from empmanage import Empmanage
class Main:
    @staticmethod
    def login():
        eid=input("Enter the user id=")
        epass=input("Enter the password=")
        if eid=="admin" and epass=="1234":
            return True
        else:
            print("Invalid Id or Password")

    def view(self):
        em=Empmanage
        while True:
            print("1. for Add Emp")
            print("2. for Display")
            print("3. Update Emp")
            print("4. Search Emp")
            print("5. Delete Emp")
            print("6. Exit.....")
            ch=int(input("Enter the choice="))
            if ch==1:
                em.addEmp()
            if ch==2:
                em.displayEmp()    
            if ch==3:
                em.updateEmp()
            if ch==4:
                em.searchEmp()
            if ch==5:
                em.deleteEmp()
            elif ch==6:
                print("Thank you..")
                break
            else:
                print("Enter valid choice.")
m=Main()  
if Main.login():
    m.view()           


