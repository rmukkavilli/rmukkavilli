class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9


def preorder(root):
    if root == None:
        return
    # recursion Pre order
    preorder(root.left)
    preorder(root.right)
    print(root.val)


    # IN order 



root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(preorder(root))