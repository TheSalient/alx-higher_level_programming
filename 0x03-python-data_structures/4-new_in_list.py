def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    elif idx >= 0 or idx < len(my_list):
        copList = my_list[:]
        copList[idx] = element
        return copList
    else:
        return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)