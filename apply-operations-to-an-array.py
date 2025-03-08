from typing import List

# class Solution:
#     def applyOperations(self, nums: List[int]) -> List[int]:
#         non_zero = []
#         zero = []
#
#         for i in range(0, len(nums) -1):
#             if nums[i] == nums[i+1]:
#                 non_zero.append(nums[i] * 2) if nums[i] * 2 != 0 else zero.append(0)
#                 nums[i + 1] = 0
#             else:
#                 non_zero.append(nums[i]) if nums[i] != 0 else zero.append(0)
#
#         non_zero.append(nums[-1]) if nums[-1] != 0 else zero.append(0)
#         return non_zero + zero

class Solution:
    def applyOperations(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        return [num for num in nums if num != 0] + [0] * nums.count(0)



ans = Solution().applyOperations([1,2,2,1,1,0])
print(ans)