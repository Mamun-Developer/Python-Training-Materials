# name,age,you
# hridoy,22,gh
# al,44,gsdl
# mamun,24,gsdl
# shofi,434,gsfsf
# kal,44e,gsdlsdfsd

matrix = [
    ["name","age","gender"],
    ["hridoy","22","male"],
    ["soni","25","female"],
    ["al","23","male"],
    ["tom","32","male"],
]

with open("csvExampmle.csv","rt") as file:
    for row in file.readlines():
        row = row.strip("\n")
        values = row.split(',')
        print(values)

def func():
    a = 10
    return a

result = func()