from typing import List



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        to_pop = []
        for i in range(0, len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                to_pop.append(i)

        for i in range(0, len(to_pop)):
            intervals.pop(to_pop[i]-i)

        return intervals
        





print(Solution().merge([[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]))


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if not intervals:
#             return []

#         # Step 1: Sort intervals based on start time
#         intervals.sort(key=lambda x: x[0])
#         merged = [intervals[0]]

#         # Step 2: Iterate and merge
#         for current in intervals[1:]:
#             last = merged[-1]
#             if current[0] <= last[1]:  # Overlap detected
#                 last[1] = max(last[1], current[1])  # Merge
#             else:
#                 merged.append(current)

#         return merged

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.