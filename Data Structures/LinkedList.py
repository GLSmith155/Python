# Linked List Data Structure.
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

# We will use this class as a contructor for all linked lists we may create.
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
    
    # Linked List Append Method         
    def append(self, value):
        new_node = Node(value)
        # If the linked list is empty make the new node have both the head and tail point at it.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # The new node is placed at tail.next
            self.tail = new_node      # Now the new node is the tail
        self.length += 1
        return True       # This method doesn't require true, but soon we will write another method that calls on this method, and it will need True.    
    
    # Linked List Pop Method.
    def pop(self):
        # If the linked list is empty just return none.
        if self.length == 0:
            return None
        
    
# The below my_ll variable first calls the LinkedList class and passes it the value 4. The LL is initialized, then the Node class creates a node of value 4.
# The next lines of code in LinkedList define head, tail, and length. LinkedList(4) creates a linked list with a single node of value 4.
my_ll = LinkedList(4)
print(my_ll.head.value)
print(my_ll.length)


 
 # Lets call the above append method and then print out the tail and length
my_ll.append(2)
 
print("This is the current tail: ", my_ll.tail.value)  # Output is 2
print("This is the current head: ", my_ll.head.value)  # Output is 4
print("This is the current length: ", my_ll.length)    # Output is 2
    
