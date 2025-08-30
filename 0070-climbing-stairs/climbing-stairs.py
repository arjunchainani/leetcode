class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1 # for the first step, there's only one way to traverse it (base case 1)
        if n > 1:
            dp[1] = 2 # for the second step, there's two ways to traverse it (base case 2)

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]