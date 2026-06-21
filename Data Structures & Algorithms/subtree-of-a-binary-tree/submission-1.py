# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # seach the node with the same value
        queue = deque()
        possible_roots =[]

        if not root:
            return False
        
        queue.append(root)
        begin_node: TreeNode | None = None
        
        target = subRoot.val

        while queue:
            node = queue.popleft()

            if node.val == target:
                begin_node = node
                possible_roots.append(begin_node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not possible_roots:
            return False
        
        # compare subtrees

        for begin_node in possible_roots:
            stack = [(begin_node, subRoot)]

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
            

