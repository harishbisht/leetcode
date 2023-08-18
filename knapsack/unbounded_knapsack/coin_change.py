# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

import math
class Solution(object):

    def find(self, coins, amount):
        if amount in self.memory:
            return self.memory[amount]
        if amount == 0:
            return 0
        minimum = math.inf
        for c in coins:
            if amount-c < 0:
                continue
            minimum = min(self.find(coins, amount-c) + 1, minimum)
        self.memory[amount] = minimum
        return minimum

    def coinChange(self, coins, amount):
        self.memory = dict()
        result = self.find(coins, amount)
        if result == math.inf:
            return -1
        return result



coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))


coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
