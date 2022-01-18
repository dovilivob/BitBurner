arr = [0, 9, 8, -1, 5, -4, 7, 9, -2, 6, 6, 9, -6, -2, 2,
       8, -7, -5, -8, -10, -2, 5, -5, 4, -3, -5, 5, 0, -6, 1]



def main():
    positives = []
    for i in range(len(arr)-1):
        n = arr[i]
        p = arr[i+1]
        if n < 0 and p > 0 and n + p >= 0:
            arr[i] = n+p
            positives.append(i+1)

    positives.sort(reverse=True)
    for p in positives:
        del arr[p]


    arr.remove(0)


main()
main()
main()
main()
print(arr)


result = 0
for element in arr:
    if element > 0:
        result += element
    else:
        break
    
print(result)