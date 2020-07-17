"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# from queue import Queue
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the left child's `insert` method 
                self.left.insert(value)
        # otherwise, value >= Node's value 
        else:
            # we need to go right 
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it 
                self.right = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the right child's `insert` method 
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not


    def contains(self, target):
        #Check if the root value is the target

        if self.value ==  target:  
        #if it is, return True(the number is contained in the tree),
            return True
        # no more needs to be done

        # if the target is not the root, then check if the target is 
        # bigger than the current value
        if target > self.value:
        # if it is, check if the right of the current value is empty or not
            if self.right is None:
        # if it is empty, return False(there are no more numbers to check, and thus the number is not in the tree)
                return False
        # if there is a next node, then return a recursion and repeat the method, this time with the next node as the value
            else: 
                return self.right.contains(target)
        # now check the left side
        # if the target is smaller than the current value:
        # check if the next node is empty or not
        if target < self.value:
        # if it is empty, return False (nothing else to search for)
            if self.left is None:
                return False
        # if it is not empty, return a recursion and repeat the method for the left side
            else:
                return self.left.contains(target)


    # Return the maximum value found in the tree

    # Recursive version:

    # def get_max(self):
    # # check the biggest number in the tree
    # # if the next right node is empty, then the biggest node is the root
    #     if self.right is None:
    #         # return that value 
    #         return self.value
    # # if there is another number, return a recursion to check the next node
    #     else:
    #         return self.right.get_max()


    # # iterative version:

    # # def get_max(self):
      
    # #     # keep a current pointer to keep track of where we are in the tree
    # #     current = self
    # #     # iterate down the right child of the current node
    # #     while current.right is not None:
    # #         # until we no longer have a right child to go to next
    # #         current = current.right
    # #     return current.value

    


    # # recursive way:

    # # Call the function `fn` on the value of each node
    # def for_each(self, fn):

    #     # call the anonymous function on self.value
    #     fn(self.value)
    #     # if this node has a left child
        
    #     if self.right is not None:
    #         # pass the anonymous function to it
    #         self.right.for_each(fn)
    #     #if this node has a right child
        
    #     if self.left is not None:
    #         # pass the anonymous function to it
    #         self.left.for_each(fn)


    # # iterative way DFT: 

    # # def for_each(self, fn):
    # #     # DFT: Last In First Out (LIFO)
    # #     # we'll use a stack

    # #     stack = []
    # #     stack.append(self)

    # #     # so long as our stack has nodes in it,
    # #     # there's more nodes to traverse

    # #     while len(stack) > 0:
    # #         # pop the top node from the stack
    # #         current = stack.pop()

    # #         # add the current node's right child first
    # #         if current.right:
    # #             stack.append(current.right)
            
    # #         # add the current node's left child
    # #         if current.left:
    # #             stack.append(current.left)

            
    # #         # Call the anonymous function
    # #         fn(current.value)

    # #     # iterative way BFT: 
    # # def for_each(self, fn):
    # #     from collections import dequeue
    # #     # BFT : First In First Out (FIFO)
    # #     # we'll use a queue to facilitate ordering

    # #     queue = deque()
    # #     queue.append(self)

    # #     # continue to traverse as long as there are 
    # #     # nodes in the queue

    # #     while len(queue) > 0:
    # #         current = queue.popleft()

    # #         if current.left:
    # #             queue.append(current.left)

    # #         if current.right:
    # #             queue.append(current.right)

    # #         fn(current.value)






    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if self.left is not None:
    #         self.left.in_order_print(node)
    #     print(self.value)

    #     if self.right is not None:
    #         self.right.in_order_print(node)
    #     # print(self.value)
    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     if node is None:
    #         return
        
    #     queue = Queue()

    #     queue.enqueue(node)

    #     while len(queue) > 0:
            
    #         node = queue.dequeue()

    #         print(node.value)

    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
       
    #     if node is None:
    #         return

    #     stack = Stack()

    #     stack.push(node)

    #     while len(stack) > 0:

    #         node = stack.pop()

    #         print(node.value)

    #         if node.left:
    #             stack.push(node.left)
    #         if node.right:
    #             stack.push(node.right)






    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass


