from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n

        nums = [num for row in grid for num in row]

        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
                break
            seen.add(num)

        for i in range(1, total_numbers + 1):
            if i not in nums:
                missing = i
                break

        return [duplicate, missing]


# Example test cases
sol = Solution()
# print(sol.findMissingAndRepeatedValues([[1, 3], [2, 2]]))  # Output: [2, 4]
print(sol.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))  # Output: [9, 5]
