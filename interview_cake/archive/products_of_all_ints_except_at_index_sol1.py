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

# my solution
list_of_integers = [1, 7, 3, 4]

def get_products_of_all_ints_except_at_index(list_of_integers):
    list_of_products = []

    for index, number in enumerate(list_of_integers):
        print(index, number)

        new_list = list_of_integers[:]
        print(new_list)
        new_list.remove(number)
        print(new_list)

        product = 1

        for x in new_list:
            product *= x

        list_of_products.append(product)
        print(product)

    return list_of_products


products = get_products_of_all_ints_except_at_index(list_of_integers)
print(products)
