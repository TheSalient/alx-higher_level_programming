def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    elif idx >= 0 or idx < len(my_list):
        copList = my_list[:]
        copList[idx] = element
        return copList
    else:
        return my_list
