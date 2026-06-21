# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def is_same_tree(self, p, q):
        stack = [(p, q)]

        while stack:
            node_a, node_b = stack.pop()

            if not node_a and not node_b:
                continue
            
            if not(node_a and node_b and node_a.val == node_b.val):
                break
            
            stack.append((node_a.right, node_b.right))
            stack.append((node_a.left, node_b.left))
        else:
            return True
        
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # seach the node with the same value
        queue = deque()

        if not root:
            return False
        
        if not root and not subRoot:
            return True
        
        if root and not subRoot:
            return True
        
        queue.append(root)
        begin_node: TreeNode | None = None
        
        target = subRoot.val

        while queue:
            node = queue.popleft()
            # we can use any traversal, but if the value exists then apply the is_same_tree
            if node.val == target:
                begin_node = node
        
                if self.is_same_tree(begin_node, subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
            

