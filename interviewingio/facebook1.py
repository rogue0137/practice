# NOT RUNNING CODE
# ARE YOU ABLE TO COME UP WITH THE ALGORITHM

"""
Given a binary tree, return the sum of values of nodes with even-valued grandparents.

Example:

        6
      /   \
     5     4 
    / \     \
   1   2     9
  
  
Sum = 1 + 2 + 9 = 12    

"""
# class Node:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right

# grandparents: for each node, the grandparent would be two levels up

# does this node have an even-valued grandparent
# if so, add to counter

def traverse_tree(root):
    queue = []  # 9 --> [4] --> [4, 1] --> [4, 1, 2] --> [4, 5] --> 6
    tree_sum = []
    # BFS
    # usually you left pop
    queue.append(root)
    while len(queue)!= 0:
        node = queue.pop() # 9 --> 4 --> 1 --> 2 --> 5 --> 6
        is_even = node.val % 2 == 0
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if is_even:
            if node.left.left:
                tree_sum += node.left.left.val
            if node.left.right:
                tree_sum += node.left.rightt.val
            if node.right.right:
                tree_sum += node.right.right.val
            if node.right.left:
                tree_sum += node.right.left.val

"""
    ["photo1", "photo2", "photo11", "photo10"] 
    should naturally sort to 
    ["photo1", "photo2", "photo10", "photo11"] 
    and NOT the default lexicographical order 
    ["photo1", "photo10", "photo11", "photo2"].

    Write a comparator function that can be used to sort an array of strings in natural order.
    int compare(String A, String B) {
      // return a positive int if A > B
      // return a negative int if A < B
      // return 0 if A == B
    };
"""

"""
1. two pointer approach
2. handling different cases:
   letter vs letter
   number vs number (special case, natural order)
   number vs letter (number comes first)
   
3. when one string ends, what to do? (comparing the lengths)

abc, x -> 
123, a -> 
aaaa, aaaa ->

talk about your idea at a high-level

write code

go over examples (manual testing)


"""

def compare(str1, str2): # photo1, photo11
    len1 = len(str1)
    len2 = len(str2)
    
    iteration_range = #whichever is less len1 or len2 
    
    for i in range(iteration_range):
        str1_char = str1[i]
        str2_char = str2[i]
        is_letter_1 = True
        is_letter_2 = True
        if is_letter1 and is_letter_2:
            str1_char > str2_char
        # ascii #s go first
        # if one is letter, one is not
            # num goes first
        # if both are num
            # if only one has a char after
                # one without extra char goes first
            # while there are still char
            
    compare lengths -> return len(str1) - len(str2)
    
            photo11
            photo11a
    
            photo11
            photo11
            
            photo11xxxx
            photo11
                

    
    # p h o t o 1 1 -- ones
    # p h o t o 2 0 -- 0 -- ones and t 