from typing import List

class Solution(object):
    def maxProduct(self, nums):
        res1 = [0 for i in range(len(nums))]
        res2 = [0 for i in range(len(nums))]


        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            if i == 0:
                res1[i] = nums[i]
                res2[i] = nums[i]
            else:
                res1[i] = max(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
                res2[i] = min(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
        
        return max(max(res1), max(res2))

ans = Solution().maxProduct(nums = [0, 2 , 0])
print(ans)


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.