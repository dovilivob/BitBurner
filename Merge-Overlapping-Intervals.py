# Merge Overlapping Intervals
# You are attempting to solve a Coding Contract. You have 15 tries remaining, after which the contract will self-destruct.


# Given the following array of array of numbers representing a list of intervals, merge all overlapping intervals.

arr = [[13, 15], [4, 9], [23, 29], [10, 15], [1, 5], [18, 21], [22, 29], [11, 20], [
    24, 30], [1, 2], [24, 25], [16, 24], [4, 13], [19, 26], [10, 18], [10, 12]]

# Example:

# [[1, 3], [8, 10], [2, 6], [10, 16]]

# would merge into[[1, 6], [8, 16]].

# The intervals must be returned in ASCENDING order. You can assume that in an interval, the first number will always be smaller than the second.

# Python3 program to merge overlapping Intervals
# in O(n Log n) time and O(1) extra space


def mergeIntervals(arr):

    # Sorting based on the increasing order
    # of the start intervals
    arr.sort(key=lambda x: x[0])

    # array to hold the merged intervals
    m = []
    s = -10000
    max = -100000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]

        # 'max' value gives the last point of
        # that particular interval
        # 's' gives the starting point of that interval
        # 'm' array contains the list of all merged intervals

        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        print("The Merged Intervals are :", end=" ")
        for i in range(len(m)):
            print(m[i], end=" ")


# Driver code
mergeIntervals(arr)

# This code is contributed
# by thirumalai srinivasan


