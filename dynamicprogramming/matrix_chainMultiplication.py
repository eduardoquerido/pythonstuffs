"""
Implementation of the Matrix Chain Multiplication problem
using Dynamic Programming (Tabulation vs Memoization)
to see the minimum required
"""
# Python program using memoization
import sys

# Dynamic Programming
dp = [[-1 for i in range(100)] for j in range(100)]


# Function for matrix chain multiplication
def matrixChainMemoised(array, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(
            dp[i][j],
            matrixChainMemoised(array, i, k)
            + matrixChainMemoised(array, k + 1, j)
            + array[i - 1] * array[k] * array[j],
        )

    return dp[i][j]


def matrixChainOrder(array, length):
    i = 1
    j = length - 1
    return matrixChainMemoised(array, i, j)


# Driver Code
array = [40, 20, 30, 10, 30]
length = len(array)
print("Minimum number of multiplications is", matrixChainOrder(array, length))
