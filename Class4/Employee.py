class Employee:
    def __init__(self, name, age, color, gender, salary):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.salary = salary

    def getSalary(self):
        return self.salary

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getColor(self):
        return self.color

    def getGender(self):
        return self.gender

    def setSalary(self, salary):
        self.salary = salary

    def setName(self, name):
        self.name = name

    def setGender(self, gender):
        self.gender = gender

    def setColor(self, color):
        self.color = color

    def setAge(self, age):
        self.age = age

if __name__ == "__main__":
    empList = list()

    emp1 = Employee("Bobby", 17, "Black", "Male", 30000)
    emp2 = Employee("Hilary", 67, "White", "Female", 40000)
    emp3 = Employee("Clinton", 32, "Black", "Female", 50000)
    emp4 = Employee("Tom", 37, "White", "Male", 60000)
    emp5 = Employee("Al", 27, "Black", "Male", 70000)

    empList.append(emp1)
    empList.append(emp2)
    empList.append(emp3)
    empList.append(emp4)
    empList.append(emp5)

    for emp in empList:
        print(emp.getName(), emp.getSalary())
