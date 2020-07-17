from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.list = DoublyLinkedList()
    
    

    def append(self, item):
        #First check if there is anything in the list
        if len(self.list) == 0:
            # if there is nothing, then the item is appended 
            # to the head using the method from dll
            self.list.add_to_head(item)

            # The current item becomes the head
            self.current = self.list.head


        # If there are items in the list and the capacity 
        # is higher than the current number of items in the list
        elif self.capacity > self.list.length:
            # if there is still space, add the new item to the end of the list
            self.list.add_to_tail(item)

        # Check if there is no more capacity to add new items in the list,
        elif self.capacity <= self.list.length:

            # check if there are more items in the list
            if self.current.next is not None:
                # if there are more items in the list and 
                # if capacity is at list length or higher, replace  the  first item (oldest) with the new item  
                # that is being insterted

                self.current.value = item

                # move current to the next node, so that the next item
                # inserted replaces that one (since it becomes the oldest)

                self.current = self.current.next

            else:
                #replace the current(which was the next) with the newest item
               
                self.current.value = item

                self.current = self.list.head

        
      

    def get(self):

        ring_buffer = []

        # keep track of the current item, in order to do a loop
        current = self.list.head

        while current:
            # add current value to the list
            ring_buffer.append(current.value)

            # move the current item to the next, so it appends it
            # to the list

            current = current.next
        return ring_buffer
         



    ### Check if there are items in the list

    ## if there are none, append the new item and make it head
