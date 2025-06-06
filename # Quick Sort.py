# Quick Sort

unsorted_list = [5, 2, 7, 3, 8, 1]

def quick_sort(list_):
    if len(list_) <= 1:
        return list_
    else:
        pivot = list_.pop()
        greater = []
        less = []
        for i in (0, len(list_)-1):
            if list_[i] > pivot:
                greater.append(list_[i])
            else:
                less.append(list_[i])
            list_ = quick_sort(less) + [pivot] + quick_sort(greater)
            print("partial sort: ", list_)
        return list_

print(unsorted_list)
sorted_list = quick_sort(unsorted_list.copy())
print(sorted_list)