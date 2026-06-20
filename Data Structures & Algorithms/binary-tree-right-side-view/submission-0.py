# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        if there is one in the right so add the right and ignore the left
        if we ignore the left the left children are not going to appear
        1.
      2    3.
    1     4  5.
  6      8.
 2.
 Always is the first element that enters first in the queue in each level begining 
 from the right and is not null
        """
        queue = deque()

        if root:
            queue.append(root)
        result = []

        while len(queue) > 0:

            size = len(queue)

            for i in range(size):
                # do something
                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    # 3
                    queue.append(node.right)
                if node.left:
                    # 2
                    queue.append(node.left)

            # 3, 2

        return result