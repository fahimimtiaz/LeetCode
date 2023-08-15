def sort_by_last_character(s):
    return s[-1]

my_list = ['apple', 'banana', 'cherry', 'date', 'fig']

my_list.sort(key=sort_by_last_character)

print(my_list)