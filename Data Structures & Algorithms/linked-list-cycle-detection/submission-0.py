# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()
        i = 0
        while node:

            if hasattr(node, "index"):
                return True

            node.index = i

            node = node.next

            i += 1

        return False
        