class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = white_count = blocks[:k].count('W')
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1

            min_operations = min(min_operations, white_count)
            if min_operations == 0:
                return 0
        return min_operations


ans = Solution().minimumRecolors(blocks = "WBBWWBBWBW", k = 7)
print(ans)