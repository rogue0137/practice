# You have a list of integers, and for each index you want to find the product of every 
# integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers 
# and returns a list of the products.

# This passes all tests cases, but is inefficient. 
def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Cannot find the products of a list with less than two integers')

    products_of_all_ints_except_at_index = []
    
    for index in range(len(int_list)):

        nums_on_left = None
        nums_on_right = None
        
        if index > 0:
            nums_on_left = int_list[:index]
        if index < len(int_list):
            nums_on_right = int_list[index + 1:]
        
        if nums_on_left and nums_on_right:
            all_nums = nums_on_left + nums_on_right
        elif nums_on_left:
            all_nums = nums_on_left
        else:
            all_nums = nums_on_right
        
        product = all_nums[0]
        for num in all_nums[1:]:
            product *= num
        products_of_all_ints_except_at_index.append(product)


    return products_of_all_ints_except_at_index

# Time Complexity:
# - This is O(N^2) because we have one outer loop. Then, within that loop, we both slice and iterate through the loop again!
# - This is no bueno

# Space Complexity
# - O(N) because we have to create a list as big as the original list 


# LAST TO FIRST PROCESSING: 
# - for i in range(len(int_list) - 1, stop_argument, step_argument)
# - for i in range(len(int_list) - 1, -1, -1)
#   - where the -1 used as step_argument tells us to iterated from back to front
#    - example: instead of iterating 1, 2, 3 in list [1, 2, 3], we'd iterate 3, 2, 1
#   - where the -1 used as stop_argument, we basically stay "don't go to -1, stop at index 0"

# This is the optimal solution
def get_products_of_all_ints_except_at_index(int_list):
    
    len_of_int_list = len(int_list)
    
    if len_of_int_list < 2:
        raise IndexError('Cannot find the products of a list with less than two integers')

    products_of_all_ints_except_at_index = [None] * len_of_int_list

    # moving front to back
    product_before_index = 1
    for i in range(len_of_int_list):  
        products_of_all_ints_except_at_index[i] = product_before_index
        product_before_index *= int_list[i]
        
    # moving back to front
    product_after_index = 1
    for i in range(len_of_int_list - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_after_index
        product_after_index *= int_list[i]
    

    return products_of_all_ints_except_at_index

# Time complexity
# - we're traversing the list 2N times now, which gets reduced to just N because constants are 
#   ignored, thus O(N)
# Space complexity
# - O(N) because we have to create a list as big as the original list 

# QUESTION 1:
# What if you could use division? Careful—watch out for zeroes!

# Great imports
from functools import reduce
from operator import mul

def get_products_of_all_ints_except_at_index(int_list):
    # Check if the list contains at least two integers
    if len(int_list) < 2:
        raise IndexError('Cannot find the products of a list with less than two integers')
    
    # Calculate the total product of all elements in the list
    total_product = reduce(mul, int_list)
    
    # Initialize the result list with zeros
    products_of_all_ints_except_at_index = [0] * len(int_list)
    
    # If the total product is zero, it means there's at least one zero in the list
    if total_product == 0:
        # Find the indices of zeros
        zero_indices = [i for i, x in enumerate(int_list) if x == 0]
        
        # If there's exactly one zero, calculate the product for its index
        if len(zero_indices) == 1:
            zero_index = zero_indices[0]
            # Calculate the product excluding the zero
            products_of_all_ints_except_at_index[zero_index] = reduce(mul, (x for i, x in enumerate(int_list) if i != zero_index))
        # If there's more than one zero, all the products will be zero, so we return the original 
        # products_of_all_ints_except_at_index we initialized with 0s
    else:
        # Divide the total product by each element to get the product of all other integers
        # Note: We are using floor division here (//) because 1) we want to ensure we always have whole numbers
        #  instead of floating-point numbers and 2) it's a best practice
        #  However, using products_of_all_ints_except_at_index = [total_product / i for i in int_list]
        #  will still result in you passing all test cases on Interview Cake
        products_of_all_ints_except_at_index = [total_product // i for i in int_list]
    
    return products_of_all_ints_except_at_index
