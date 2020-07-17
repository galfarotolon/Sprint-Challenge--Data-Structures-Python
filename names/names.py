import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

## Runtime: 5.59 seconds


### NEW CODE: 

## Create a new instance of BSTNode, passing in the file 
# we want to check 

#start with the first name of the file, then search it 
# using the BST until all names have been checked for

name_tree = BSTNode(names_1[0])

# check for every name in the file
for name in range(len(names_1)):
    # loop through and insert every name 
    # in the tree to check 
    # if it contains duplicates later on
    name_tree.insert(names_1[name])

## Loop through the second file of names, and check if
# that file contains duplicate names with the first file

for name in names_2:
    #check the recently inserted values in the tree
    # if the name is a duplicate, store it in the empty list above

    if name_tree.contains(name):
        # if the name is duplicate, add to the list
        duplicates.append(name)


## NICE!! RUNTIME IS 0.10 SECONDS

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
