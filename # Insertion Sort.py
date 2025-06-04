# Insertion Sort
# Only one that uses a while loop
# Does less comparision and is faster

unsorted_list = [5, 2, 7, 3, 8, 1]

def insertion_sort(list_):
    for i in range(1, len(list_)):
        key = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > key:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
    return list_



print(unsorted_list)
sorted_list = insertion_sort(unsorted_list.copy())
print(sorted_list)