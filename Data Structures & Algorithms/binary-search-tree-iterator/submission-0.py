# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []

        # init the stack, the last element is the min val
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left

    def next(self) -> int:
        
        node = self.stack.pop()
        value = node.val
        
        right = node.right

        while right:
            self.stack.append(right)
            right = right.left
        
        return value

    def hasNext(self) -> bool:
        return bool(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()