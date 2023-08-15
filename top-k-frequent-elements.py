from typing import List

class Solution:
    def topFrequentElement(nums: List[int], k: int):
        freq = {}

        for elmnt in nums:
            if elmnt in freq:
                freq[elmnt] += 1
            else:
                freq[elmnt] = 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        final_arr = []
        
        i = 1
        for key in sorted_freq:
            if i<=k:
                final_arr.append(key)
                i += 1
            else:
                break

        return final_arr

print(Solution.topFrequentElement(nums = [1,1,1,2,2,3], k = 2))