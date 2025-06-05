# Insertion Sort
# Only one that uses a while loop
# Does less comparision and is faster

unsorted_list = [5, 2, 7, 3, 8, 1]

def insertion_sort(list_):
    for cards_position in range(1, len(list_)):
        current_card = list_[cards_position]
        left_cards_position = cards_position - 1
        left_card = list_[left_cards_position]
        while left_cards_position >= 0 and left_card > current_card:
            list_[left_cards_position + 1] = list_[left_cards_position]
            left_cards_position -= 1
        list_[left_cards_position + 1] = current_card
    return list_



print(unsorted_list)
sorted_list = insertion_sort(unsorted_list.copy())
print(sorted_list)