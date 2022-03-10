def sort_list(unsorted_list):
    n = len(unsorted_list)
    sorted_list = unsorted_list[:]
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
            j += 1
        i += 1
    return sorted_list
