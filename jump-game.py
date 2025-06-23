from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums or len(nums)==1:
            return True
        
        got_zero = False
        zero_index = len(nums)

        for i in range(len(nums)-2, -1, -1):
            if got_zero and zero_index - i < nums[i]:
                got_zero = False
                # print("zero index", zero_index)
                # print("Jump index", i)
            
            if nums[i] == 0:
                if not got_zero:
                    zero_index = i
                got_zero = True
                # print("Got Zero")
    
        return False if got_zero else True

print(Solution().canJump([2,0,1,0,1]))







# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.