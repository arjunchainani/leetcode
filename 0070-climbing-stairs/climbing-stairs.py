# options: 1 or 2 steps; unique combinations of 1 and 2 that add up to n

# initialize number of steps left to n
# - 1 step
#   - 1 step
#   - 2 steps
# - 2 steps
#   - 1 step
#   - 2 steps

# subproblems: solving the problem for (n - 1) from taking 1 step as your initial decision
#              solving the problem for (n - 2) from taking 2 steps as your initial decision
#              add these subproblems together

# keep traversing until the number of steps left = 0 --> valid combination; increase counter variable
# or keep traversing until the number of steps left is < 0 --> invalid combination; stop traversing this branch
# 

def computeNumTraversals(n, dp):
   # base case 1: 1 step left
    if n == 1:
        return 1

    # base case 2: 2 steps left
    if n == 2:
        return 2

    # "base case" 3: number of traversals for the number of steps left is a value we've already computed
    if n in dp:
        return dp[n]

    # recursive case
    numberOfTraversals = computeNumTraversals(n - 1, dp) + computeNumTraversals(n - 2, dp)
    dp[n] = numberOfTraversals
    return numberOfTraversals

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}

        return computeNumTraversals(n, dp)


# sample input: n = 5
# - computeNumTraversals(4, dp) --> 5 (dp[4] = 5)
#   - computeNumTraversals(3, dp) ---> 3 (dp[3] = 3)
#     - computeNumTraversals(2, dp)  ---> 2
#     - computeNumTraversals(1, dp)  ---> 1
#   - computeNumTraversals(2, dp) --> 2
# - computeNumTraversals(3, dp) --> from cache = 3