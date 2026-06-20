# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
            queue.append(root)

        count_level = 0

        while len(queue) > 0 :
            count_level += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            
        return count_level