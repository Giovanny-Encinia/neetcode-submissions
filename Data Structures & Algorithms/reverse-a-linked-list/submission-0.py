# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = str(self.val)
        n = self.next
        while n:
            result += f", {n.val}"
            n = n.next
            
        return result

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        print(previous)

        return previous
        