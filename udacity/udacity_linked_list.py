"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the node at a certain position.
The "insert" function will add an node to a particular
spot in the list.
"delete" will delete the first node with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
    def get_position(self, position):
        """Get an node from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_node, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd nodes."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current 
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

# Test cases
# Set up some nodes
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList() # alternately you can also pass e1 here
ll.append(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
assert ll.head.next.next.value == 3
# Should also print 3
assert ll.get_position(3).value == 3

# Test insert
ll.insert(e4,3)
# Should print 4 now
assert ll.get_position(3).value == 4


# Test delete
ll.delete(2)
# Should print 1 now
assert ll.get_position(1).value == 1
# Should print 4 now
assert ll.get_position(2).value == 4
# Should print 3 now
assert ll.get_position(3).value == 3