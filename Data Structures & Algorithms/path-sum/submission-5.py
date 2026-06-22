# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # there is no leaf or the next node destriy the sum
        def dfs(root, remainder):
            if not root:
                return False
            
            remainder -= root.val

            # this is a leaf
            if not root.left and not root.right and remainder == 0:
                return True
            
            if dfs(root.left, remainder):
                return True
            if dfs(root.right, remainder):
                return True

            return False
        
        return dfs(root, targetSum)


