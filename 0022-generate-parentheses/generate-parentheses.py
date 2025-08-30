class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = {}
        dp[0] = [""]
        dp[1] = ["()"] # base case 1

        if n > 1:
            for i in range(2, n + 1):
                dp[i] = []

                for j in range(i):
                    for left in dp[i - 1 - j]:
                        for right in dp[j]:
                            dp[i].append("(" + left + ")" + right)
        
        return dp[n]