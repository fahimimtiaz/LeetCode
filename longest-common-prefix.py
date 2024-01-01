from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        print(strs)
        shortest = strs[0]
        longest = strs[-1]


        for i, char in enumerate(shortest):
            if char != longest[i]:
                return shortest[:i]

        return shortest 

result = Solution().longestCommonPrefix(strs =  ["flower", "flow", "flight"])
print(result)