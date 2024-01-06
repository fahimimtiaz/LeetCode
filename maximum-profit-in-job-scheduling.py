from typing import List
from bisect import bisect_left


class Solution:
    #Copied Solution from chatGPT, Not solved by me

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        n = len(jobs)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            start, end, p = jobs[i]

            # Binary search to find the next job with start time greater than or equal to the current job's end time
            next_job_index = bisect_left(jobs, (end, float('-inf'), float('-inf')))

            # Calculate the maximum profit by considering or skipping the current job
            max_profit = p + dp[next_job_index] if next_job_index < n else p

            # Update the dp array with the new maximum profit for the current job
            dp[i] = max(max_profit, dp[i + 1] if i + 1 < n else 0)

        return dp[0]


ans = Solution().jobScheduling( startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
print(ans)

# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.

# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6