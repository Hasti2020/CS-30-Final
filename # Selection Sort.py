# Selection Sort

unsorted_list = [5, 2, 7, 3, 8, 1]

def selection_sort(list_):
    for i in range(len(list_) -1):
        smallest_index = i
        for j in range(i+1, len(list_)):
            if list_[j] < list_[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            list_[smallest_index], list_[i] = list_[i], list_[smallest_index] #shortcut
            #smallest = list_[smallest_index]
            #list_[smallest_index] = list_[i]
            #list_[i] = smallest
        print("partial sort: ", list_)
    return list_

print(unsorted_list)
sorted_list = selection_sort(unsorted_list.copy())
print(sorted_list)