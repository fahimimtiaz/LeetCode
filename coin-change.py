from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            print("a: "+str(a))
            for c in coins:
                if a - c >= 0:
                    dp[a] =min(dp[a], 1 + dp[a-c])
                    print(dp[a])

        # print(dp)
        

ans = Solution().coinChange(coins = [1,3,4,5], amount = 7)
# print(ans)


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0