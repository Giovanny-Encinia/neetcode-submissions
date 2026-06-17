# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        previous = None
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        max_val = float("-inf")
        
        while slow:
            max_val = max(max_val, slow.val + previous.val)
            slow = slow.next
            previous = previous.next
        
        return max_val
            