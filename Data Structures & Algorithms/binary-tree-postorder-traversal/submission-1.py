# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse_list(self, array):
        
        left = 0
        right = len(array) - 1

        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        traversal = []

        while node or stack:

            if node:
                traversal.append(node.val)

                if node.left:
                    stack.append(node.left)
                
                node = node.right
            else:
                node = stack.pop()
        
        self.reverse_list(traversal)

        return traversal