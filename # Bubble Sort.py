# Bubble Sort

unsorted_list = [5, 2, 7, 3, 8, 1]

def bubble_sort(list_):
    switch = 0
    for i in range(len(list_)-1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j+1]: #compare the two cards next to each other
                list_[j], list_[j+1] = list_[j+1], list_[j] #switch!
                switch += 1
            print("partial sort: ", list_)
    print("Switch: ", switch)
    return list_

print(unsorted_list)
sorted_list = bubble_sort(unsorted_list.copy())
print(sorted_list)