def sort_by_last_character(nums):
    sorted_list = sorted(nums)
 
    previous = sorted_list[0]
    if previous !=0 :
        return 0
    for i in range(1, len(sorted_list)):
        if sorted_list[i] - previous == 1:
            previous = sorted_list[i]
        else:
            return previous + 1

    return len(sorted_list)

print(sort_by_last_character([1]))