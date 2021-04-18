def listIndexRem():
    names = list()

    names.append("1")
    names.append("2")
    names.append("3")
    names.append("4")
    names.append("5")
    names.append("6")
    names.append("7")
    print(names)

    newLIst = list()
    for i in range(len(names)):
        if i != 3:
            newLIst.append(names[i])
    print(newLIst)

#listIndexRem()


def inpuStDetails():
    subNum = dict()

    tS = int(input("How many students? : "))
    for i in range(tS):
        stname = input("Name: ")
        stAge = int(input("Age: "))
        subNum[stname] = stAge
    print(subNum)

subNum = {
    "1":"st1",
    "2":"st2"
}

subNum2 = subNum.copy()

subNum2["1"]="hi"
print(subNum2)
print(subNum)

# print(subNum.get('1'))

# print(subNum.items())

# print(subNum.keys())

# subNum.clear()
# print(subNum)

# removes specific key
# popped = subNum.pop('2')
# print(popped)

#removes last item
# subNum.popitem()
# print(subNum)
