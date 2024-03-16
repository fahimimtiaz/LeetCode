from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_freq = {0: 1}
        cumulative_sum = 0

        for num in nums:
            print("num: ", num)
            cumulative_sum += num
            print("cumulative_sum: ", cumulative_sum)

            count += sum_freq.get(cumulative_sum - goal, 0)
            print("Count: ", count)

            sum_freq[cumulative_sum] = sum_freq.get(cumulative_sum, 0) + 1
            print("sum_freq: ", sum_freq, "\n")

        return count


ans = Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2)
# ans = Solution().numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0)
print(ans)
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
