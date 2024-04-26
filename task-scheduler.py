from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = [0] * 26

        for task in tasks:
            task_count[ord(task) - ord('A')] += 1

        task_count.sort(reverse=True)
        max_count = task_count[0] - 1
        idle_slots = max_count * n

        for i in range(1, len(task_count)):
            idle_slots -= min(task_count[i], max_count)

        idle_slots = max(0, idle_slots)

        return len(tasks) + idle_slots


ans = Solution().leastInterval(tasks =["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1)
print(ans)

# Example
# 1:
#
# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
#
# Output: 8
#
# Input: tasks = ["A", "C", "A", "B", "D", "B"], n = 1
#
# Output: 6
#
# Example
# 3:
#
# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 3
#
# Output: 10
#
