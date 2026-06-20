# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        traversal = []
        node = root

        while node or stack:
            if node:
                traversal.append(node.val)

                if node.right:
                    stack.append(node.right)

                node = node.left
            else:
                node = stack.pop()
        
        return traversal