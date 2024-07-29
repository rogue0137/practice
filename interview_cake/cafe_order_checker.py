# I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. 
# All the customer orders get combined into one list for the kitchen, where they should be handled 
# first-come, first-served.

# Recently, some customers have been complaining that people who placed orders after them are getting 
# their food first. Yikes—that's not good for business!

# To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

# The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
# The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
# Each customer order (from either register) as it was finished by the kitchen. (served_orders)
# Given all three lists, write a function to check that my service is first-come, first-served. 
# All food should come out in the same order customers requested it.

# We'll represent each customer order as a unique integer.

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    # iterate through take_out_orders and dine_in_orders
    # if neither, take_out_orders[take_out_index], nor dine_in_orders[dine_in_index]
    # is the next spot in served_orders, served_orders is out of order
    
    take_out_index = 0
    dine_in_index = 0
    
    for current_order in served_orders:
        
        # need to make sure indexes aren't out of range
        if take_out_index < len(take_out_orders):
            current_take_out = take_out_orders[take_out_index]
        if dine_in_index < len(dine_in_orders):
            current_dine_in = dine_in_orders[dine_in_index]
        
        if take_out_index < len(take_out_orders) and current_order == current_take_out:
            take_out_index += 1
        elif dine_in_index < len(dine_in_orders) and current_order == current_dine_in:
            dine_in_index += 1
        else: 
            return False
    
    # Check for extra orders
    if take_out_index == len(take_out_orders) and dine_in_index == len(dine_in_orders):
        return True
    else:
        return False
    
# Time Complexity
# - it is N because we have to literally iterate through the entire size of served orders
# - operations inside the loop (checking conditions, incrementing indices) are constant 
#   time operations, O(1), and do not depend on the size of the input lists

# Space Complexity
# - the function uses a fixed amount of additional space to store indices (take_out_index, dine_in_index) 
#   and temporary variables (current_take_out, current_dine_in). These do not scale with the size of the 
#   input lists; thus, they contribute a constant amount of space, O(1)
# - However, the MAIN reason it's 0(1) is that the function does not create any new data structures that grow with the size of the input, 
#   so its space complexity is considered O(1)


# QUESTION 1: This assumes each customer order in served_orders is unique. How can we adapt this to handle lists of customer orders 
# with potential repeats?
# ANSWER 1: It really depends. Do we need repeats to be in order or can they be anywhere? 

# QUESTION 2: Our implementation returns True when all the items in dine_in_orders and take_out_orders are first-come first-served 
# in served_orders and False otherwise. That said, it'd be reasonable to raise an exception if some orders that went into the 
# kitchen were never served, or orders were served but not paid for at either register. How could we check for those cases?

# ANSWER 2: I'd basically add "check order integrity" as a function at the beginning so that we throw an error before trying to asses if
# take_out and dine_in orders are in the appropriate order. It could be something like:

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    check_order_integrity(take_out_orders, dine_in_orders, served_orders)

    # Rest of code above...


def check_order_integrity(take_out_orders, dine_in_orders, served_orders):
    # Combine take-out and dine-in orders
    all_orders = take_out_orders + dine_in_orders
    
    # Convert lists to sets for easier comparison
    all_orders_set = set(all_orders)
    served_orders_set = set(served_orders)
    
    # Check if any order was taken but not served
    missing_orders = all_orders_set - served_orders_set
    if missing_orders:
        raise ValueError(f"Orders were taken but not served: {missing_orders}")
    
    # Check if any order was served but not taken
    extra_served_orders = served_orders_set - all_orders_set
    if extra_served_orders:
        raise ValueError(f"Orders were served but not taken: {extra_served_orders}")

# Question 3: Our solution iterates through the customer orders from front to back. 
# Would our algorithm work if we iterated from the back towards the front? 
# Which approach is cleaner?

# Answer 3: Front to back is cleaner than back to front approach. Our questions asks about first-come, first-serve
# so it automatically lends it self to a front order. However, if we needed to iterate the other way, we could. It would
# just make for much more confusing code.
