from typing import List

class Solution:
    def longest_increasing_subseq(self, nums: List[int]):
        result = 1
        max_result = 1

        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1]:
                result += 1
            else:
                max_result = max(result, max_result)
                result = 1
        max_result = max(result, max_result)

        return max_result
        

ans = Solution().longest_increasing_subseq(nums = [10,9,2,5,3,7,101,18])
print(ans)
