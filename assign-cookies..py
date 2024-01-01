from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        counter = 0
        cookies_size = len(s)

        for i in range(len(g)):
            child = g[i]
            for j in range(cookies_size):
                cookie = s[0]
                if cookie>=child:
                    counter+=1
                    s.pop(0)
                    cookies_size -= 1
                    break
                else:
                    s.pop(0)
                    cookies_size -= 1
                
        return counter

solution = Solution().findContentChildren(g = [10,9,8,7], s = [7])
print(solution)