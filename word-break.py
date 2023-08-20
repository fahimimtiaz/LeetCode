from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(1, n + 1):
            print(i)
            print("-")
            for j in range(i):
                print(j)
                print(s[j:i])
                # Check if the substring s[j:i] (from index j to i-1) is in the wordDict and dp[j] is True.
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
            print("=")
            print(dp)
        return dp[n]

ans = Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
print(ans)
