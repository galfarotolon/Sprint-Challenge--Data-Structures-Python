"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


        # Had to add a delete method in ListNode for the tests to pass
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)

        # Increase the length of the list by 1 when adding a new node
        self.length += 1

        # In the case the list is initially empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #the new node becomes the head of the list
            # set the current head's prev to the new node
            new_node.next = self.head
            # set the new node's next to the current head
            self.head.prev = new_node
            # reassign self.head to point to the new node
            self.head = new_node


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
       value = self.head.value
       self.delete(self.head)
       return value
            

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        new_node = ListNode(value, None, None)

         
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:

            #Flip everything from add_to_head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return None
        # store a reference to node we're  going to move
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return None
        # store a reference to node we're  going to move
        value = node.value
        
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
            # check if the node is the head of the list
        elif self.head is node:
            self.head = node.next
            node.delete()

            #check if node is tail of the list
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
            #if its not either head or tail, delete without changing references
        else: 
            node.delete()
        
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    # def get_max(self):
    #     # init a variable that will keep track of  the largest element we've seen so far

    #     current_max = self.head.value
    #     current = self.head.next
    #     #Checks if there are more values in the list
    #     while current is not None:
    #     # checks if the current value is bigger than the maximum value in the list
    #         if current.value > current_max:
    #             # if it is, then make that the new biggest value in the list
    #             current_max = current.value
    #         # Now check the next value and do the same process to find out if there are bigger values than the current
    #         current = current.next
    #     # If it is  the only value, then it is the current maximum value and it is returned as the current_max
    #     return current_max


    def get_max(self):
        #start at the head
        start = self.head
        # store the start value on a variable so we can update if a bigger number appears in the list
        max_val = start.value
        # loop through list until the end
        while start is not None:
            # compare start's value to the max_value
            if start.value > max_val:
                # update max value to be the start value
                max_val = start.value

            # update start to be the next value 
            start = start.next
        
        return max_val