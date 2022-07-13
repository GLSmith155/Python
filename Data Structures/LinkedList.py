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

# Contructor for linked lists.
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
    
    # Pop Method for removal of the last item in the list and return its value for possible use with temp.
    def pop(self):
        # If the linked list is empty just return none.
        if self.length == 0:
            return None
        temp = self.head  # temp is now equal to the 1st item.
        pre = self.head   # pre is now equal to the 1st item.
        # While we have 2 or more items in the linked list temp = next. Then walk pre up a step. Then temp up a step.
        while(temp.next):     # temp is now the 2nd item.
            pre = temp        # pre is now the 2nd item
            temp = temp.next  # temp is now the 3rd item. This will continue until temp.next is None, in which case the while loop is no longer true. 
        self.tail = pre       # Sets the new tail to the 2nd to last item.
        self.tail.next = None # Makes the original last item None. But, if we only have one item this won't work.
        self.length -= 1  
        if self.length == 0:  # If we have decrimented down to 0, but we didn't the first time, then we must only have one item in our linked list.
            self.head = None  
            self.tail = None  # Now if there is only one item left it is gone.
        return temp
        
    # Remove first item in the linked list and return the removed value for potential use with temp.
    def pop_first(self):
        if self.length == 0:  # If the linked list is already empty just return none.
            return None       
        temp = self.head   # temp value that equals the first item.
        self.head = self.head.next  # Set a new head value as the 2nd value in the list.
        temp.next = None            # Make the former head None.
        self.length -= 1 
        if self.length == 0:        # If we only had one value to begin with this value will now reach 0, so just set the tail to None as head is already None.
            self.tail = None
        return temp.value
        
    # Prepend method to append a node to the beginning of the list.
    def prepend(self, value):
        new_node = Node(value) # Create a node.
        if self.length == 0: # If there are no items in the list new_node will be set to head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # The new_nod's next value is the current head.
            self.head = new_node       # The head is now changed to new_node.
        self.length += 1
        return True   # We will create a method later that will need this method to return True.
    
    
# The below my_ll variable first calls the LinkedList class and passes it the value 4. The LL is initialized, then the Node class creates a node of value 4.
# The next lines of code in LinkedList define head, tail, and length. LinkedList(4) creates a linked list with a single node of value 4.
my_ll = LinkedList(4)
print("This is the LinkedList(4) head: ", my_ll.head.value) # Output is 4
print("This is the LinkedList(4) length: ", my_ll.length)   # Output is 1


 
 # Lets call the above append method and then print out the tail and length
my_ll.append(2)
#print("This is the current head: ", my_ll.head.value)  # Output is 4
#print("This is the current tail: ", my_ll.tail.value)  # Output is 2
#print("This is the current length: ", my_ll.length)    # Output is 2

my_ll.append(3) # Adds a 3 to the end.
print("\nThis is the append 3 tail: ", my_ll.tail.value)  # Output is 3
print("This is the append 3 length: ", my_ll.length)    # Output is 2
my_ll.pop()    # Removes the 3 from the Linked List.
print("\nThis is the after pop head: ", my_ll.head.value)  # Output is 4
print("This is the after pop tail: ", my_ll.tail.value)  # Output is 2
print("This is the after pop length: ", my_ll.length)    # Output is 2

my_ll.prepend(1)
print("\nThis is the after prepend 1 head: ", my_ll.head.value)  # Output is 1
print("This is the after prepend 1 length: ", my_ll.length)    # Output is 3   

print("\nThis is the return value after pop_first is used: ", my_ll.pop_first())  # Output is 1, and 1 is no longer in the ll.
