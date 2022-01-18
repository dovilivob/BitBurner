# Goal: Get the minimum value from top to bottom

Triangle = [
    [4],
    [2, 8],
    [8, 7, 9],
    [3, 7, 9, 5],
    [2, 8, 3, 3, 6],
    [8, 6, 5, 2, 4, 5]
]

allResult = []

index = []


for i in range(2 ** (len(Triangle)-1)):
    result = bin(i).replace('0b', '')
    if len(result) < len(Triangle)-1:
        result += ('0'*(len(Triangle)-1-len(result)))
    index.append(result)

# print(index)

for i in index:
    result = 4
    n = 0
    for r in range(len(Triangle)-1):
        result += Triangle[r+1][n]
        n += int(i[r])
    allResult.append(result)

allResult.sort()
print(allResult[0])
