from typing import List


class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        first_security_row_found = False
        previous_row_security_count = 0
        current_row_security_count = 0

        for bn in bank:
            for char in bn:
                if char == '1':
                    current_row_security_count += 1

            if not first_security_row_found and current_row_security_count:
                first_security_row_found = True
            else:
                result += current_row_security_count * previous_row_security_count

            previous_row_security_count = current_row_security_count if current_row_security_count else previous_row_security_count
            current_row_security_count = 0

        return result


ans = Solution().numberOfBeams(bank =["000","111","000"])
print(ans)

        