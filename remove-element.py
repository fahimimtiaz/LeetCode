from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


# Example usage:
nums = [3, 2, 2, 3]
val = 3
result_length = Solution().removeElement(nums, val)
print(result_length)  # Output: 2
print(nums[:result_length])  # Output: [2, 2]