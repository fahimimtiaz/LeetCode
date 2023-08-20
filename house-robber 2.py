from typing import List

class Solution(object):
    def houseRobber(self, nums):

        if not nums:
            return 0
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if n == 2 or n==3:
            return max(nums)
        nums_with_first = nums[:-1]
        nums_without_first = nums[1:]


        #With First element
        dp = [0] * (n-1)
        dp[0] = nums_with_first[0]
        dp[1] = max(nums_with_first[0], nums_with_first[1])
        
        for i in range(2, n-1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums_with_first[i]) 
        with_first_house = dp[n - 2]

        #Without First element
        dp = [0] * (n-1)
        dp[0] = nums_without_first[0]
        dp[1] = max(nums_without_first[0], nums_without_first[1])
        
        for i in range(2, n-1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums_without_first[i]) 
        without_first_house = dp[n - 2]
        
        return max(with_first_house, without_first_house)

ans = Solution().houseRobber(nums = [1,2,1,1])
print(ans)


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12