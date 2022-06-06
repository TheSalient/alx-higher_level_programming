def new_in_list(my_list, idx, element):
    copList = []
    for i in my_list:
        copList.append(i)
    if idx >= 0 or idx < len(my_list):
        copList[idx] = element
        return copList
