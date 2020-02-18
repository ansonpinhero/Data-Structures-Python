class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,root):
        self.root = Node(root)

    """
    Method for preorder traversal
    root -> left -> right

    """

    def preorder(self,root,traversal):
        if root:
            traversal += (str(root.value) + "-")
            traversal = self.preorder(root.left, traversal)
            traversal = self.preorder(root.right, traversal)
        return traversal

    """
    Method for inorder traversal
    left -> root -> right

    """
    def inorder(self,root,traversal):
        if root:
            traversal = self.inorder(root.left, traversal)
            traversal += (str(root.value) + "-")
            traversal = self.inorder(root.right, traversal)
        return traversal

    """
    Method for postorder traversal
    left -> right -> root

    """

    def postorder(self,root,traversal):
        if root:
            traversal = self.postorder(root.left, traversal)
            traversal = self.postorder(root.right, traversal)
            traversal += (str(root.value) + "-")
        return traversal

"""
Creating Tree

"""

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

"""
Displaying tree

"""

print("         1       ")
print("       /   \     ")
print("      2     3    ")
print("     / \   / \   ")
print("    4   5 6   7  ")

"""
Displaying preorder,postorder,inorder traversals

"""
print("Preorder traversal   >> ",tree.preorder(tree.root,""))
print("postorder traversal  >> ",tree.postorder(tree.root,""))
print("inorder traversal    >> ",tree.inorder(tree.root,""))


