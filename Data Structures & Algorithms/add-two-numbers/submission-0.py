# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = f"{self.val}, "

        next = self.next
        while next:
            result += f"{next.val}, "
            next = next.next
        
        return result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        9 9 9 
        9 9 9

        1 9  9 8
        """

        dummy = ListNode()
        result = dummy
        carry = 0
        i = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            suma = v1 + v2 + carry
            digit = suma % 10
            carry = suma // 10
            result.next = ListNode(digit)
            
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            

        print(dummy.next)
        return dummy.next
