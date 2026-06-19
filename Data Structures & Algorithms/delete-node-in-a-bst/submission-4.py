# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search_min(self, root):
        node = root

        while node and node.left:
            node = node.left
        
        return node
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # here is the number
            print("number found", root.val)
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_value = self.search_min(root.right)
                print(min_value.val)
                root.val = min_value.val
                root.right = self.deleteNode(root.right, min_value.val)
        
        return root
