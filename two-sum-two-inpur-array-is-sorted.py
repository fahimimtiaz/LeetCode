from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            rest = target - numbers[i]
            numbers[i] = 9999
            if rest in numbers:
                return [i + 1, numbers.index(rest) + 1]


ans = Solution().twoSum(numbers = [0,0,1,2], target = 0)
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