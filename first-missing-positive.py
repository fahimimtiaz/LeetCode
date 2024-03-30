from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Mark non-positive integers as 0
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # Mark visited indices
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Find the first positive missing integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


ans = Solution().firstMissingPositive(nums=[3,4,-1,1])
print(ans)

# Example 1:
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.