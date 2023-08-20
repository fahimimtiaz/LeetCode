from itertools import permutations

def permutation(nums, start = 0):

    if start == len(nums) - 1:
        print(nums)
    else:
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            permutation(nums, start + 1)    
            nums[start], nums[i] = nums[i], nums[start] 
print(permutation([1,2,3]))