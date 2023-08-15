def check_distinct(x):
    new_list = []
    for i in x:
        new_list.append(i)
        
    for i in range(len(x)-1, -1, -1):
        int_in_str = str(x[i])[::-1]
        reverse_int = int(int_in_str)
        new_list.append(reverse_int)

    list_set = set(new_list)
    return len(list_set)



print(check_distinct([1,13,10,12,31]))
