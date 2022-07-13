# Linked List Data Structures.
# Time Complexity - Adding to the end is O(1)           Removing the end is O(n) as we have to iterate up the list.
#                   Adding to the beginning is O(1)     Removing the beginning is O(1)
#                   Adding to center is O(n)            Removing from center is O(n)

# Compared to lists:      Lists are better at pop end and looking up by index. list is O(1) for both and ll is O(n).
#                         Linked Lists are better at pop first and removing first where it's O(1), while lists are O(n).

# A linked list under the hood is a nested dictionary like below.
head = { "value": 11, "next": { "value": 3, "next": { "value": 23, "next": { "value": 7, "next": None }}}}

# Now for an actual linked list.
# Constructor for our nodes.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# We will use this class as a contructor for all linked lists we may create, therefore we'd only have to type it once.
class LinkedList:
    # Creates a new Node. 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #  Creates a new Node. Adds node to end.
    # def append(self, value):
    
    # Creates a new Node. Inserts node at beginning.
    # def prepend(self, value):
    
    # Creates a new Node. Insert node at whatever index we want.
    # def insert(self, value):
    
# The below my_ll variable first calls the LinkedList class and passes it the value 4. The LL is initialized, then the Node class is called that creates 4 nodes.
# The next lines of code in LinkedList define head, tail, and length.
my_ll = LinkedList(4)
print(my_ll.head.value)  #Output is 4
