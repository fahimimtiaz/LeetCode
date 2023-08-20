class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            print(stack)

            if c not in dict:
                stack.append(c)
                continue
            if not stack or stack[-1] != dict[c]:
                return False
            stack.pop()

        return not stack


ans = Solution().isValid(s = "()[()])")
print(ans)