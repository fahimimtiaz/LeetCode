
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         row_size = int(len(s)/2) + 1
#         matrix = [[0 for _ in range(row_size)] for _ in range(numRows)]
#         row = 0
#         column = 0

#         if len(s) <= 2 or numRows==1:
#             return s

#         forward = True
#         for i, char in enumerate(s):
#             # print("Row: ", row, "Column: ", column)
#             if forward:
#                 if numRows - row != 1:
#                     matrix[row][column] = char
#                     row += 1
#                 else:
#                     matrix[row][column] = char
#                     forward = False

#             if not forward:
#                 if row != 0:
#                     matrix[row][column] = char
#                     row -= 1
#                     column += 1
#                 else:
#                     matrix[row][column] = char
#                     row += 1
#                     forward = True
            
#         new_str = ""
#         for row in matrix:
#             for value in row:
#                 if value != 0:
#                     new_str += value
#                     # print(value, end = " ")
#             # print()

#         return new_str



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        current_row = 0
        going_down = False

        # print(rows)

        for char in s:
            print(rows)

            rows[current_row] += char
            # Change direction if we're at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1


        return ''.join(rows)




print(Solution().convert("PAYPALISHIRING", 5))


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