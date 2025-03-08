class Solution:
    def coloredCells(self, n: int) -> int:
        if n <= 1:
            return n
        return n*n + (n-1)*(n-1)


ans = Solution().coloredCells(n = 4)
print(ans)