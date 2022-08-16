from tkinter import N
from turtle import pos
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len =  len(nums)

        prefix = [1] * nums_len
        postfix = [1] * nums_len

        # For Prefix
        products = 1
        for i in range(nums_len):
            products  = products * nums[i]
            prefix[i] = products
        
         # For Postfix
        products = 1
        for i in range(nums_len-1, -1 , -1):
            products  = products * nums[i]
            postfix[i] = products
 
        ans = [1] * nums_len
        for i in range(nums_len):
            if i==0:
                ans[i] = postfix[i+1]
            elif i==nums_len-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1] * postfix[i+1]
        return ans


    def productExceptSelfVersion2(self, nums: List[int]) -> List[int]:
        nums_len =  len(nums)

        prefix = 1
        postfix = 1
        ans = [1] * nums_len

        for i in range(nums_len):
            ans[i] *= prefix
            prefix *= nums[i]
 
        products = 1
        for i in range(nums_len-1, -1 , -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
        

ans = Solution().productExceptSelfVersion2(nums = [1,2,3,4])
print(ans)



# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]