class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    def reverse_list(self, node, prev):
        
        #check if list has nodes or if it is empty
        # This is the way to exit the loop when using recursion

        if self.head is None:
            return
        
         # If there are nodes, then begin the recursion in each node

         #store the current node as the head of the list, as starting point
        current_node = self.head


        # set the previous node to be none for now
        previous_node = None


       # loop through the list as long as there is something in it

        while current_node is not None:

            # make a variable to point the current node to the next one

           nextNode = current_node.next_node

        # the current now becomes the previous node
           current_node.next_node = previous_node

           # previous becomes current

           previous_node = current_node

           # current becomes next

           current_node = nextNode

           # once exit the loop
           # set the head to the previous node, which is the last
           # node in the list before it was reversed

        self.head = previous_node

          




   