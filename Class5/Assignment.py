class penguins:
    def __init__(self,name, age, color, walk,stop="yes"):
        self.age = age
        self.name = name
        self.color = color
        self.walk = walk
        self.stop = stop
    def getWalk(self):
        return f"{self.name*2} is {self.walk}ing"
    def notWalking(self):
        return "{0} is {1}ing".format(self.name,self.walk)
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def getColor(self):
        return self.color

if __name__ == "__main__":
    empList = list()
    firstpenguin = penguins("Hasan", 30, "Black","walk","no")
    firstpenguin1 =penguins("Hasan1", 30, "black", "not walk")

    empList.append(firstpenguin)
    empList.append(firstpenguin1)
    for emp in empList:
        print(emp.getName(),emp.getAge(),emp.getColor(),emp.notWalking())