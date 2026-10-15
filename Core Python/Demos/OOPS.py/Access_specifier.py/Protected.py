class Emp:
    def __init__(self,id,name,sal):
        self._id = id
        self._name = name
        self._sal = sal

    def getId(self):
        return self._id
    def setId(self, newid):
        self._id=newid

    def __str__(self):
        return f"Id={self._id}Name={self._name}Sal={self._sal}"

class Hr(Emp):
    def __str__(self):
        print(self._id)
        return super().__str__()

e1 = Emp(12,"Swaraj",12340)
print(e1.getId())
e1.setId(19)
print(e1.getId())
h1 = Hr(1,"Smriti",34643)
print(h1._name)
                