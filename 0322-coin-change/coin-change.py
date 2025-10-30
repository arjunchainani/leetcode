# combinations of integer coin values that sum up to amount; minimum size combination

# approach 1: backtracking / DFS
# keep track of the amount left that we need to cover with the new coins to the combination
# init at amount

# - 1 cent coin
#   - 1 cent coin
#   - 2 cent coin
#   - 5 cent coin
# - 2 cent coin
# - 5 cent coin

# base cases: 1) amount_left = 0 --> successful coin combination; update global min if necessary
# base cases: 2) amount_left < 0 --> unsuccessful coin combination; backtrack 
# time complexity: O(3^N)

# approach 2: cache / DP memoization --> top down DP
# time complexity: O(N)

# approach 3: bottom up DP
# -- base case 1: f(0) -> 0
# -- base case 2: f(coin_values) = 1
# -- base case 3: if f(value < min(coin_value)) == -1 

# [1, 2, 5] - coins; amount = 11
# f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 2, f(5) = 1, f(6) = 2
# recurrence relation: f(n < amount) => min([1 + f(n - coin_value) for each coin_value])

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [None] * (amount + 1)

        # edge case
        if amount == 0:
            return 0

        # base cases
        dp[0] = 0
        for coin_value in coins:
            if coin_value < len(dp):
                dp[coin_value] = 1
        
        # dp = [0, 1, 1, 2, 2, 1, 2, None, None, None, None, 3]

        # iterate through and build out the solution by solving the individual subproblems
        for n in range(amount + 1):
            if dp[n] is None:
                min_paths_per_coin_value = [amount + 1] * len(coins)
                for coin_value in coins:
                    if n - coin_value >= 0 and dp[n - coin_value] != -1:
                        min_paths_per_coin_value.append(1 + dp[n - coin_value])
                
                dp[n] = min(min_paths_per_coin_value)
                if dp[n] == amount + 1: # default case if nothing in the min_paths list was updated (i.e. no paths)
                    dp[n] = -1
        
        return dp[amount]