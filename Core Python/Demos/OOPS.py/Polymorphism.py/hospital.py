class Hospital:
    def __init__(self, name, location, beds):
        self.name = name
        self.location = location
        self.beds = beds

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getLocation(self):
        return self.location
    def setLocation(self, newlocation):
        self.location = newlocation

    def getBeds(self):
        return self.beds
    def setBeds(self, newbeds):
        self.beds = newbeds

    def display(self):
        print(f"Name={self.name}\tLocation={self.location}\tBeds={self.beds}")


class Department(Hospital):
    def __init__(self, name, location, beds, departmentName):
        super().__init__(name, location, beds)
        self.departmentName = departmentName

    def getDepartmentname(self):
        return self.departmentname
    def setDepartmentname(self, newdepartmentname):
        self.departmentname = newdepartmentname    

    def display(self):
        super().display()
        print(f"Department={self.departmentName}")

class EmergencyDepartment(Hospital):
    def __init__(self, name, location, beds, doctors):
        super().__init__(name, location, beds)
        self.doctors = doctors

    def getDectors(self):
        return self.doctors
    def setDoctors(self, newdoctors):
        self.doctors= newdoctors

    def display(self):
        super().display()
        print(f"Doctors={self.doctors}")

h1 = Hospital("Sasun", "Pune", 500)
d1 = Department("Sahyadri", "Mumbai", 400, "Cardiology")
e1 = EmergencyDepartment("Apollo", "Mumbai", 600, "Emergency", 25)

h1.display()
d1.display()
e1.display()

