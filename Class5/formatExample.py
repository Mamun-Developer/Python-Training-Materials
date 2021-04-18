class StringClone:
    def __init__(self,value):
        self.myString = value

    def getString(self):
        return self.myString

    def __str__(self):
        return self.myString

    def __format__(self, first):
        find = "["
        updatedString = ""
        for char in range(len(self.myString)):
            if self.myString[char]=="[":
                updatedString = updatedString + first
            else:
                updatedString = updatedString + self.myString[char]
        return updatedString

strClone = StringClone("This [is my name")
print(strClone)
res = strClone.__format__("10")
print(res)



