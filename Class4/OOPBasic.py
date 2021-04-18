class ClassName:
    def __init__(self,nam,age):
        print(self)
        self.nam = nam
        self.age = age

    def getProperties(self,mult):
        return self.nam,self.age*mult

    def getName(self,param2):
        return param2

    def getName2(self):
        return self.nam


ob1 = ClassName("name",32)
ob2 = ClassName("nam23e",21)
ob3 = ClassName("name23",322)