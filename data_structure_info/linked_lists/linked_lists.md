# Linked Lists


Memorize how to create a linked list: [my example in python](https://github.com/rogue0137/general/blob/master/online_practice_sites/udacity/udacity_linked_list.py)

## Basics for a LinkedList
- Nodes class
- LinkedList class
- Single vs. doubly linked lists --> basic gist: Node's of a single have `.next` attributes, doubly has `.next` and `.prev` attributes
- Be able to create the following methods in your LinkedList class
    - append Node (to end of linked list)
    - insert Node (to specific place w/in linked list)
    - get_position of Node
    - delete Node
- Know:
    - `curr` is key. Use it to help you figure out where you are in the LinkedList. It's used to solve most LinkedList problems
    - `while` loops are prevalent in solving many LinkedList problems
    - Linked list problems are *alllll* about pointers; many of the questions you get asked about LinkedLists will require you to have two or more pointers so you can most appropriately traverse the LinkedList(s)
    - Cycles are a thing in linked lists
        - cycle: if two LinkedLists every become one
        - how do you tell if it's a cycle? two-pointers of different speeds eventually meet up
- Some things you'll get asked to do:
    - Reverse the list: this is basically switching the pointers, you'll need to create a prev for this too
    - Do two LinkedLists meet? (Cycles!)
    
