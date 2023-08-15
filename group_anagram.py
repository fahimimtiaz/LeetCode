from typing import List

class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        freq_dict = {}

        for item in strs:
            word = ''.join(sorted(item))
            if word in freq_dict:
                freq_dict[word].append(item)
            else:
                freq_dict[word] = [item]
        
        final_list = []
        for value in freq_dict.values():
            final_list.append(value)


        return final_list

print(Solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]