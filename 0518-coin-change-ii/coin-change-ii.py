# combinations that add up to a sum --> backtracking / DFS

# approach 1: naive backtracking
# amount_left = amount
# - 1 cent coin
#   - 1 cent coin
#       - 1 cent coin
#       - 2 cent coin
#       - 5 cent coin
#   - 2 cent coin
#   - 5 cent coin
# - 2 cent coin
#   - 1 cent coin
#   - 2 cent coin
#   - 5 cent coin
# - 5 cent coin
#   - 1 cent coin
#   - 2 cent coin
#   - 5 cent coin
# traverse this decision tree until we hit a base case:
#       1) amount_left = 0 --> successful combination; increment counter
#       2) amount_left < 0 --> unsuccessful combination = backtrack
# Time complexity: O(len(coins) ^ amount)

# approach 2: top-down DP
# cache previous computations (e.g. f(3)) to avoid redoing them
# dp dictionary that maps amount_left values to the total number of subcombinations
# time complexity: O(amount)
# space complexity: O(amount)

# approach 3: bottom-up DP
# f(0) = 1, f(min(coin_value)) = 1, f(< min(coin(value))) = 0, 
# f(2) = 1 --> (1 + 1), (2) 
# f(3) = 2 --> (1 + 1 + 1), (1 + 2)
# f(4) = 3 --> (1 + 1 + 1 + 1), (1 + 1 + 2), (2 + 2)
# f(5) = 4 --> (1 + 1 + 1 + 1 + 1), (2 + 1 + 1 + 1), (2 + 2 + 1), (5)

# recurrence relation:
# f(5) = f(5 - coins[0]) + unique(f(5 - coins[1])) + unique(f(5 - coins[2])) 

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1) # [1, 1, 2, 2, 3, 4]

        # base cases
        dp[0] = 1
        smallest_coin = min(coins)

        # [1, 1, 1, 1, 1, 1, ... 1]

        if amount < smallest_coin:
            return dp[amount]

        for i in range(1, smallest_coin):
            dp[i] = 0
        
        dp[smallest_coin] = 1

        coins = sorted(coins)

        for i in range(len(coins)):
            # build out each subproblem one by one
            for n in range(smallest_coin + 1, len(dp)):
                if n - coins[i] >= 0:
                    dp[n] += dp[n - coins[i]]

        return dp[amount]

# amount = 5, coins = [1, 2, 5]
# dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = 2, dp[4] = 3, dp[5] = 4