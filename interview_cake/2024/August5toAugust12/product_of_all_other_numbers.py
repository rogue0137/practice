# You have a list of integers, and for each index you want to find the product of every 
# integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers 
# and returns a list of the products.

# The following is still not the Interview Cake solution, but it's good enough for me!
def get_products_of_all_ints_except_at_index(int_list):

    len_of_int_list = len(int_list) # 5
    if len_of_int_list < 2:
        raise IndexError('Need at least two integers')
    
    list_of_before_products = [1] * len_of_int_list 
    list_of_after_products = [1] * len_of_int_list
    

    before_product = 1
    # go forward through the list
    for forward_index in range(len_of_int_list):
        if forward_index > 0: 
            before_product *= int_list[forward_index - 1]
            list_of_before_products[forward_index] = before_product
        
    after_product = 1
    # go backward through the list
    for backward_index in range(len_of_int_list - 1, -1, -1):
        if backward_index < len_of_int_list - 1:
            after_product *= int_list[backward_index + 1]
            list_of_after_products[backward_index] = after_product
        

    list_of_products = []
    for i in range(len_of_int_list):
        full_product = list_of_before_products[i] * list_of_after_products[i]
        list_of_products.append(full_product)
        
    return list_of_products

# The main difference between the above solution and the the Interview Cake solution and I start our lists.
# Interview Cake does this:
#  list_of_before_products = [None] * len_of_int_list 
#  list_of_after_products = [None] * len_of_int_list
# However, I do the following:
#  list_of_before_products = [1] * len_of_int_list 
#  list_of_after_products = [1] * len_of_int_list
# This means I'm "off by one", but my code adjusts for it. 
