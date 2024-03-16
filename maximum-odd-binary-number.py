from typing import List


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = 0
        count_zero = 0

        for i in range(len(s)):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one += 1

        output = (count_one - 1) * '1' + count_zero * '0' + '1'

        return output


ans = Solution().maximumOddBinaryNumber(s="01010101000001")
print(ans)
# Input: s = "010"
# Output: "001"
# Input: s = "0101"
# Output: "1001"