class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dic = {}
        for i in nums:
            if i not in freq_dic:
                freq_dic[i] = 1
            else:
                freq_dic[i] += 1
        
        
        for i in freq_dic:
            if freq_dic[i] == 1:
                return i

