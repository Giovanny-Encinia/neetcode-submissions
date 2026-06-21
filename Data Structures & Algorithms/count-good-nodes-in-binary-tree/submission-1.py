# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, current_max):
            if not root:
                return 0
            
            count = 0

            if current_max <= root.val:
                current_max = root.val
                count += 1
            
            count += dfs(root.left, current_max)
            count += dfs(root.right, current_max)

            return count
        
        return dfs(root, root.val)