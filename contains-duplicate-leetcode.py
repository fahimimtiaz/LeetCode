from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
            
        return False
        
ans = Solution().containsDuplicate(nums = [1,2,3,4])
print(ans)


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true