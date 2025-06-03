# Simple Sort
# CS 30
# Only one that makes a new list!

unsorted_list = [5, 2, 7, 3, 8, 1]

# Without min function:

def simple_sort2(original_list):
    new_list = []
    for i in range(len(original_list)):
        smallest_index = 0
        #for j in range(1, len(original_list), 1):
        for j in range(len(original_list)-1, 0, -1):  #starts from the end and goes back
            if original_list[smallest_index] > original_list[j]:
                smallest_index = j
        smallest = original_list[smallest_index]
        new_list.append(smallest)
        original_list.remove(smallest)
    return new_list

sorted_list = simple_sort2(unsorted_list.copy()) # In order for the org not to be empty at the end
print(unsorted_list)
print(sorted_list)

# With using min function:

def simple_sort1(original_list):
    new_list = []
    for i in range(len(original_list)):
        smallest = min(original_list)
        new_list.append(smallest)
        original_list.remove(smallest)
    return new_list

sorted_list = simple_sort1(unsorted_list.copy()) # In order for the org not to be empty at the end
print(unsorted_list)
print(sorted_list)

