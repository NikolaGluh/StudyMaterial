# Trees are a set of nodes and edges that connect various nodes
# Root of the tree is the top most node
# Nodes follow OOP principles, they have ancestors and descendants, parent and child nodes
# Leaf nodes are the nodes that do not have any children, which are nodes that are at the end of the tree
# Internal nodes are any nodes between the root and leaf nodes
# There is a path from every node to another node, which is a sequence of nodes and edges that connect them
# The height of a tree is the number of steps from the root to the furthest leaf node
# The level of a tree is the number of steps from the root to the node
# Every node has a key, which is a value that is used to identify the node

# Binary Tree
# A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
# Binary Search Tree (BST) is a binary tree in which each node has a key greater than all the keys in its left subtree and less than all the keys in its right subtree.

# Example of a binary tree:
#          1
#         / \
#        2   3
#       / \   \
#      4   5   6
#     / \   \ 
#    7   8   9 

# Traversal of a tree is the process of visiting each node in the tree exactly once in some order.
# There are three types of traversal: preorder, inorder, and postorder.
# Preorder traversal visits the root node first, then the left subtree, and finally the right subtree. [1,2,4,7,8,5,9,3,6]
# Inorder traversal visits the left subtree first from it's end, then the root node, and finally the right subtree. [7,4,8,2,5,9,1,3,6]
# Postorder traversal visits the left subtree first from it's end, then the right subtree, and finally the root node, for each current node. [7,8,4,9,5,2,6,3,1]

# Time complexity: O(h) where h is height of the tree. Space complexity: O(n) for storing the nodes

# Creating a node class for a tree
class Node:
    def __init__(self, id: int, ocena: float) -> None:
        self.id = id # Unique identifier for the node
        self.ocena = ocena # Value associated with the node
        self.left = None # Points to the left child of the node
        self.right = None # Points to the right child of the node

# Function for inserting a node into a tree
def insert(root: Node, id: int, ocena: float) -> Node:
    # Checking if the root is empty
    if root is None:
        return Node(id, ocena)
    # Checking if the id exists in the tree, if so, return the root node without inserting a new node
    elif root.id == id:
        return root
    else:
        # Checking if the current id is less than the root id, if so, insert it into the left subtree
        if id < root.id:
            root.left = insert(root.left, id, ocena)
        # Otherwise, insert it into the right subtree
        if id > root.id:
            root.right = insert(root.right, id, ocena)
    return root

# Function for displaying tree data (inorder traversal)
def display(root: Node) -> None:
    # Checking if the root is empty, if it's not then display the left subtree, root, and right subtree
    if root:
        display(root.left)
        print(f"ID: {root.id}, Ocena: {root.ocena}")
        display(root.right)

# Function for searching a tree
def find(root: Node, id: int) -> Node | bool:
    # Checking if the root is empty, if so, return false
    if root is None:
        return False
    # Checking if the current value of the node has the same id as the one we are searching for, if so, return true
    elif root.id == id:
        return True
    # If the id we are looking for is less than the current node id, search in the left subtree
    elif id < root.id:
        return find(root.left, id)
    # Otherwise, search in the right subtree
    elif id > root.id:
        return find(root.right, id)
        
# Function for getting the minimum value of a tree
def getMin(root: Node):
    # If the root does not exist, return +inf
    if root is None:
        return float('inf')
    # Finding the minimum value by comparing values of the left and right child nodes to the root node
    min = root.ocena
    leftMin = getMin(root.left)
    rightMin = getMin(root.right)
    if leftMin < min:
        min = leftMin
    if rightMin < min:
        min = rightMin
    return min

# Function for getting the maximum value of a tree
def getMax(root: Node):
    # If the root does not exist, return -inf
    if root is None:
        return float('-inf')
    # Finding the maximum value by comparing values of the left and right child nodes to the root node
    max = root.ocena
    leftMax = getMax(root.left)
    rightMax = getMax(root.right)
    if leftMax > max:
        max = leftMax
    if rightMax > max:
        max = rightMax
    return max

# Function for getting the level of a tree
def getLevelOfNode(root: Node, id: int, level: int = 1) -> int:
    # If the value of the node isn't in the tree, return -1
    if not find(root, id):
        print("Value not found in the tree")
        return -1
    # If the first value of the tree is the same as the one we are looking for, return the current level
    if root.id == id:
        return level
    
    # If the value we are looking for is less than the current node id, search in the left subtree and increment the level by 1
    if id < root.id:
        return getLevelOfNode(root.left, id, level + 1)
    # Otherwise, search in the right subtree and increment the level by 1
    else:
        return getLevelOfNode(root.right, id, level + 1)
    
# Function for getting the sum of all values in the tree
def getSum(root: Node) -> float:
    # If the root does not exist, return 0 for sum and counter
    if root is None:
        return 0,0
    
    # Getting the values of the left and right child nodes
    leftSum, leftCount = getSum(root.left)
    rightSum, rightCount = getSum(root.right)

    # Add value of the current node, left and right child nodes to the sum
    sum = leftSum + rightSum + root.ocena
    # Increment the counter by 1 and left and right counts
    count = leftCount + rightCount + 1

    return sum, count

# Function for getting the average of all values in the tree
def getAverage(root: Node) -> float:
    # Getting the sum and count of all values in the tree
    sum, count = getSum(root)
    # If the count is 0, return 0 for average
    if count == 0:
        return 0
    # Otherwise, return the average of all values in the tree
    return sum / count

# Function for deleting a node from the tree
def delete(root: Node, id: int) -> Node:
    # If the value does not exist in the tree, return
    if not find(root, id):
        print("Value not found in the tree")
        return root
    
    deleteHelper(root, id)

# Function for deleting a node from the tree
def deleteHelper(root: Node, id: int) -> Node:
    # If the root is empty, return root
    if root is None:
        return root
    # If the value we are looking for is less than the current node id, search in the left subtree
    if id < root.id:
        root.left = deleteHelper(root.left, id)
    # else if it's greater than the current node id, search in the right subtree
    elif id > root.id:
        root.right = deleteHelper(root.right, id)
    # Checking if the current node has no children, if so, set it to None
    elif root.left is None and root.right is None:
        root = None
    # If it has the right child, set the current node's id to the right child's successor's id and delete the right child
    elif root.right is not None:
        root.id = successor(root.right)
        root.right = deleteHelper(root.right, id)
    # If it has the left child, set the current node's id to the left child's predecessor's id and delete the left child
    elif root.left is not None:
        root.id = predecessor(root.left)
        root.left = deleteHelper(root.left, id)
    return root

# Function for getting the successor of a node
def successor(root: Node) -> int:
    # Setting the root to root's right value
    root = root.right
    # While left value exists, set the root to the left value
    while root.left is not None:
        root = root.left
    # Return the root's id
    return root.id

# Function for getting the predecessor of a node
def predecessor(root: Node) -> int:
    # Setting the root to root's left value
    root = root.left
    # While right value exists, set the root to the right value
    while root.right is not None:
        root = root.right
    # Return the root's id
    return root.id

root = Node(13, 3.45)
insert(root, 8, 4.65)
insert(root, 3, 4.95)
insert(root, 18, 3.43)
insert(root, 17, 4.23)

display(root)

print(find(root, 14)) # False

print(f"Minimum value in the tree: {getMin(root)}")
print(f"Maximum value in the tree: {getMax(root)}")

level = getLevelOfNode(root, 13)

average = getAverage(root)

print(f"Average value in the tree: {average}")

delete(root, 17)

display(root)
