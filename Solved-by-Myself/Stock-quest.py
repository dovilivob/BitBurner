# Goal: Get the maximum trade profit

# stocks = [61, 50, 161, 24, 44, 100, 170, 15, 200, 60, 113, 155, 103, 124, 10, 118, 174,
#           21, 116, 63, 81, 90, 161, 164, 68, 126, 31, 115, 150, 185, 192, 97, 23, 78, 95, 43, 78]

stocks = [116, 175, 180, 183, 39, 118, 28, 55, 56,
          35, 44, 175, 100, 161, 167, 97, 194, 130, 91]

dealLimit = 2


def noLimit():
    profit = 0
    for i in range(len(stocks)-1):
        gain = stocks[i+1]-stocks[i]
        if gain > 0:
            profit += gain

        print(profit)


def limited_two():
    profits = []
    index = []
    all = len(stocks)-2
    for x in range(all):
        for y in range(x, all):
            for z in range(y, all):
                for r in range(z, all):
                    if x != y != z != r:
                        index.append([x, y, z, r])

    # print(index)
    for i in index:
        def get(x): return stocks[i[x]]
        profits.append(get(1)+get(3)-get(0)-get(2))

    profits.sort(reverse=True)
    print(profits[0])


limited_two()
