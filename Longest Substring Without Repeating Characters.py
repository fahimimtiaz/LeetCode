def sub_string(s):
    char_index_map = {}  
    max_length = 0
    start = 0 
    
    for i in range(len(s)):
        if s[i] in char_index_map and char_index_map[s[i]] >= start:
            start = char_index_map[s[i]] + 1
        char_index_map[s[i]] = i
        max_length = max(max_length, i - start + 1)
        print(char_index_map)
        print("Max Length:")
        print(max_length)

    
    return max_length

print(sub_string("dvdfvd"))