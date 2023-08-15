def test(x):
    sorted_list = sorted(set(sorted(x)))

    if len(sorted_list) == 0:
        return 0
    result = 1
    max_result = 1
    for i in range(1,len(sorted_list)):
        if sorted_list[i] -1 == sorted_list[i-1]:
            result+=1
        else:
            max_result = max(result, max_result)
            result = 1
        
    max_result = max(result, max_result)
    return max_result

print(test([100,4,200,1,3,2]))