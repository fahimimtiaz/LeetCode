from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ascii_value = ord(target)
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2  

            # if ord(letters[mid]) > target_ascii_value:
            #     right = mid - 1 
            if ord(letters[mid]) < target_ascii_value:
                left = mid + 1  
            
            if left == right:
                return letters[left]
             
        return target_ascii_value
        

ob1 = Solution()
print(ob1.nextGreatestLetter(letters = ["c","f","j"], target = "c"))