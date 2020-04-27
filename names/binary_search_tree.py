class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None # BinarySearchTree
        self.right = None # BinarySearchTree 

    # Insert the given value into the tree
    def insert(self, value):
        # if value is smaller than current node value and left is none, 
        # create a new node to the left
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        # if value is greater or equal to current node value and right is none,
        # create a new node to the right
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        # if value is smaller than current node value, go left
        if value < self.value:
            self.left.insert(value)
        # else value is larger than current node value and goes right
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        curr_node_value = self.value
        # Base Case
        # if equal, return True!
        if target == curr_node_value:
            return True
        # if smaller and left is not None, go left 
        elif target < curr_node_value and self.left is not None:
            return self.left.contains(target)
        # if bigger and right is not None, go right
        elif target > curr_node_value and self.right is not None:
            return self.right.contains(target)
        # If all other conditions fail, return false
        else:
            return False