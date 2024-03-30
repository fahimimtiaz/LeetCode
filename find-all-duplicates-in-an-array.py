from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup_check_dic = dict()

        for i in range(len(nums)):
            if nums[i] not in dup_check_dic:
                dup_check_dic[nums[i]] = 1
                continue
            dup_check_dic[nums[i]] += 1

        result = []
        for key in dup_check_dic:
            result.append(key) if dup_check_dic[key] > 1 else None

        return sorted(result)


ans = Solution().findDuplicates(nums=  [1])
print(ans)

# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
#
# Input: nums = [1]
# Output: []