def new_in_list(my_list, idx, element):
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        it = my_list.copy()
        it[idx] = element
        return it
