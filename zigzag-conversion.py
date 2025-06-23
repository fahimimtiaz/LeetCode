
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[0 for _ in range(len(s))] for _ in range(numRows)]
        row = 0
        column = 0
        if len(s) <= 2 or numRows==1:
            return s
        
        forward = True
        for i, char in enumerate(s):
            # print("Row: ", row, "Column: ", column)
            if forward:
                if numRows - row != 1:
                    matrix[row][column] = char
                    row += 1
                else:
                    matrix[row][column] = char
                    forward = False

            if not forward:
                if row != 0:
                    matrix[row][column] = char
                    row -= 1
                    column += 1
                else:
                    matrix[row][column] = char
                    row += 1
                    forward = True
            
        new_str = ""
        for row in matrix:
            for value in row:
                if value != 0:
                    new_str += value
                    # print(value, end = " ")
            # print()

        return new_str
        

print(Solution().convert("ABC", 1))


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"