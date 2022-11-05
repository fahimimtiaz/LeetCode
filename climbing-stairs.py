class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n;
        
        a,b = 1,2

        i=3
        ans = 0
        while i<=n:
            ans = a + b
            a = b
            b = ans 
            i+=1
        return ans


ans = Solution().climbStairs(n = 5)
print(ans)