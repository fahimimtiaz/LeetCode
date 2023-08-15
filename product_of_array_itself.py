from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        nums_len =  len(nums)

        prefix = 1
        postfix = 1
        ans = [1] * nums_len

        for i in range(nums_len):
            ans[i] *= prefix
            prefix *= nums[i]
        print(ans)

        for i in range(nums_len-1, -1 , -1):
            print(i)
            print(postfix)

            ans[i] *= postfix
            postfix *= nums[i]
        print(ans)

        return ans

print(Solution.productExceptSelf(nums = [1,2,3,4]))