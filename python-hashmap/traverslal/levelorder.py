from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def levelOrder(root):
    if root is None:
        return []
    queue = deque([root])
    res = []
    while queue:
        level_len = len(queue)
        level = []
        for _ in range(level_len):
            node = queue.popleft()
            level.append(node.val)
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
        res.append(level)
    return res



root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))