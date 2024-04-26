from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        tmp = 1
        for i in range(len(digits)-1, -1, -1):
            num = num + (tmp * digits[i])
            tmp = tmp * 10

        num = str(num)
        num_list = []

        for i in num:
            num_list.append(int(i))
        return num_list

ans = Solution().plusOne(digits = [9])
print(ans)



# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].