# In order to win the prize for most cookies sold, my friend Alice and 
# I are going to merge our Girl Scout Cookies orders and enter as one unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

def merge_lists(my_list, alices_list):
    # In case either list is blank
    len_of_my_list = len(my_list)
    len_of_alices_list = len(alices_list)
    if len_of_my_list == 0:
        return alices_list
    if len_of_alices_list == 0:
        return my_list
    
    # Combine the sorted lists into one large sorted list
    new_list = []
    
    my_index = 0
    alice_index = 0
    
    while my_index < len_of_my_list and alice_index < len_of_alices_list:
        my_num = my_list[my_index]
        alice_num = alices_list[alice_index]
       
        if my_num < alice_num:
           new_list.append(my_num)
           my_index += 1
        elif my_num > alice_num:
           new_list.append(alice_num)
           alice_index += 1
        else:
            # if they are the same
            new_list.append(my_num)
            my_index += 1
            new_list.append(alice_num)
            alice_index += 1
            
    if (my_index < len_of_my_list):
        new_list.extend(my_list[my_index:])
    if (alice_index < len_of_alices_list):
        new_list.extend(alices_list[alice_index:])

    return new_list

# This is not what Interview Cake recommends, but I think it is much faster.
# I think Interview Cake just tried to convert something from a language where
# you have to define the number of spaces in a list before you can add to it.
# Python lists are automatically dynamic. Thus, I feel the above is much simpler to
# read, while maintaining Big O of O(n) for time and O(n) for space.

# Something I did not know:
# In Python YOu can do this:
def merge_sorted_lists(arr1, arr2):
    return sorted(arr1 + arr2)

# You can also do this:
import heapq

# Example sorted lists
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Merging the lists
merged_list = list(heapq.merge(list1, list2))

print("Merged List:", merged_list)
# Merged List: [1, 2, 3, 4, 5, 6, 7, 8]


# Question 1: What if we wanted to merge several sorted lists? 
# Write a function that takes as an input a list of sorted lists
# and outputs a single sorted list with all the items from each list.

def merge_multiple_lists(list_of_lists):
    number_of_lists = len(list_of_lists)

    if number_of_lists == 0:
        return []

    big_list = list_of_lists[0]

    for new_list in list_of_lists[1:]:
        big_list = merge_lists(big_list, new_list)
    
    return big_list


# Do we absolutely have to allocate a new list to use for the merged output? 
# Where else could we store our merged list? 
# How would our function need to change?

# Modifying One of the Original Lists
def merge_in_place(my_list, alices_list):
    my_list.extend(alices_list)
    my_list.sort()
    return my_list 
