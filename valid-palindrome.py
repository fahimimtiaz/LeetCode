import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert string into lower case
        lowercase_string = s.lower()
        
        #remove all non-alphanumeric characters
        lowercase_string = re.sub(r'[\W_]', '', lowercase_string)
        
        #reverse the string 
        reverse_string = lowercase_string[::-1]
        if lowercase_string == reverse_string:
            return True
        return False


ans = Solution().isPalindrome(s = "")
print(ans)


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.