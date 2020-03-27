import time

'''
There is a nested for loop.
With just one for loop that iterates through the entire list
the runtime complexity would be O(n), but because for each
entry in one list you are running through the second list
the runtime complexity is O(n^2)
'''

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates1 = []  # Return the list of duplicates in this data structure
duplicates2 = [] # used to ensure that all duplicates are found

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates1.append(name_1)

# this brings the runtime down to ~1.5 seconds
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare
        # if new < node
        if value < self.value:
            # check if empty
            if self.left == None:
                # put node in
                self.left = BinarySearchTree(value)
            # else
            else:
                # go left
                self.left.insert(value)
        # if new >= node
        else:
            # check if empty
            if self.right == None:
                # put node in
                self.right = BinarySearchTree(value)
            # else
            else:
                # go right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node is none
            # return False
        # if node.value == findvalue
        if self.value == target:
            # return True
            return True
        # else
        else:
            # if find < node.value
            if target < self.value:
                # if left exists
                if self.left:
                    # find(node.left)
                    return self.left.contains(target)
                # else
                else:
                    # return false
                    return False
            # else
            else:
                # if right exists
                if self.right:
                    # find(node.right)
                    return self.right.contains(target)
                else:
                    return False


name_tree = BinarySearchTree('m')
for name in names_1:
    name_tree.insert(name)
for name in names_2:
    if name_tree.contains(name):
        duplicates1.append(name)


# Holy shit this is quick. How do they do this so fast
# duplicates2 = [i for i in set(names_1).intersection(names_2)]



end_time = time.time()
print (f"{len(duplicates1)} duplicates:\n\n{', '.join(duplicates1)}\n\n")
# print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n") # used to ensure all duplicates are found
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
