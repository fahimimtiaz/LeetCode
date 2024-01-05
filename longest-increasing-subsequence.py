from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                print(nums[i], "-", nums[j])
                print("==")
                if nums[i] > nums[j]:
                    print("Condition Matched")
                    print(f"{nums[i]} is greater than {nums[j]}")
                    print(f"Now i: {i} and j: {j}")
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)


ans = Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
print(ans)

        