from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for data in range(1, len(nums)):

            if nums[data] != nums[data - 1]:

                nums[l] = nums[data]

                l += 1

        return l
        

ob1 = Solution()
print(ob1.removeDuplicates([1,1,2,2,3,3,4]))