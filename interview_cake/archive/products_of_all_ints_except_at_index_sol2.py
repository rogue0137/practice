# Write a function get_products_of_all_ints_except_at_index()
# that takes a list of integers and returns a list of the products.
#
# For example, given:
#
#   [1, 7, 3, 4]
#
# your function would return:
#
#   [84, 12, 28, 21]
#
# by calculating:
#
#   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
#
# Do not use division in your solution.

# actual solution

list_of_integers = [1, 7, 3, 4]

def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index


products = get_products_of_all_ints_except_at_index(list_of_integers)
print(products)
