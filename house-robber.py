from typing import List

class Solution(object):
    def houseRobber(self, nums):

        if not nums:
            return 0
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        for i in range(0, n):
            print(dp[i])
        
        return dp[n - 1]

ans = Solution().houseRobber(nums = [1,3,1,3,100])
print(ans)


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12