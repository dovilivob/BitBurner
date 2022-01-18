# Unique Paths in a Grid I
# You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


# You are in a grid with 14 rows and 13 columns, and you are positioned in the top-left corner of that grid. You are trying to reach the bottom-right corner of the grid, but you can only move down or right on each step. Determine how many unique paths there are from start to finish.

# NOTE: The data returned for this contract is an array with the number of rows and columns:

grid = [14, 13]

# Returns count of possible paths
# to reach cell at row number m and
# column number n from the topmost
# leftmost cell (cell at 1, 1)


def numberOfPaths(p, q):

    # Create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]


# Driver Code
print(numberOfPaths(grid[0], grid[1]))

# This code is contributed
# by Ankit Yadav
