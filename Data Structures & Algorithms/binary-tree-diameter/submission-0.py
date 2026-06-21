# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = 0

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        max_heigth = 1 + max(left, right)
        self.max_path = max(self.max_path, left + right)
        #print(f"max heigth: {max_heigth}, max path: {self.max_path}")
        return max_heigth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_path
        