from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = 0, 0
        for num in nums:
            current_sum = max(0, current_sum + num)
            max_sum = max(current_sum, max_sum)
            # print("Current Sum : "+str(current_sum)+"  Max Sum : "+str(max_sum))
        return max(nums) if max(nums)<0 else max_sum


ans = Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
print(ans)



# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23