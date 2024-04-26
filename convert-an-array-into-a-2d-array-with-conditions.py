from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        distinct_2d_array = [[nums[0]]]
        
        for i in range(1, len(nums)):

            for idx in range(0, len(distinct_2d_array)):
                if nums[i] not in distinct_2d_array[idx]:
                    distinct_2d_array[idx].append(nums[i])
                    break
                else:
                    if idx+1 == len(distinct_2d_array):
                        distinct_2d_array.append([nums[i]]) 
            
        return distinct_2d_array


ans = Solution().findMatrix(nums = [1,3,4,1,2,3,1])
print(ans)

        