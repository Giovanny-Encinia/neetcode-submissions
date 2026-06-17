# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        previous = None
        node = slow

        while node:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        
        head2 = previous
        node2 = head2
        node1 = head
        
        max_sum = float("-inf")

        while node2 and node1:
            max_sum = max(node1.val + node2.val, max_sum)
            node1 = node1.next
            node2 = node2.next
        
        return max_sum





        