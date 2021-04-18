matrix = [1,2,3,4]

matrix2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

arr = list()
for i in matrix2:
    for j in i:
        print(j)
        arr.append(j)
print(arr)