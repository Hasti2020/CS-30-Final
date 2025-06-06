# Insertion Sort
# Only one that uses a while loop
# Does less comparision and is faster

unsorted_list = [5, 2, 7, 3, 8, 1]

def insertion_sort(list_):
<<<<<<< HEAD
    for cards_position in range(1, len(list_)):
        current_card = list_[cards_position]
        left_cards_position = cards_position - 1
        left_card = list_[left_cards_position]
        while left_cards_position >= 0 and left_card > current_card:
            list_[left_cards_position + 1] = list_[left_cards_position]
            left_cards_position -= 1
        list_[left_cards_position + 1] = current_card
=======
    for i in range(1, len(list_)):
        key = list_[i]
        j = i + 1
        while j >= 0 and list_[j] > key:
            list_[j - 1] = list_[j]
            j -= 1
        list_[j - 1] = key
>>>>>>> 80fa7aca7b9b9a6bd5692ae12fa0c8e476886499
    return list_



print(unsorted_list)
sorted_list = insertion_sort(unsorted_list.copy())
print(sorted_list)