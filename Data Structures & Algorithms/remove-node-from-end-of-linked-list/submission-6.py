# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if not head and n > 0:
            return None

        stack = []
        
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        
        stack.pop(-n)

        dummy = ListNode()
        head = dummy

        for i in range(len(stack)):
            head.next = ListNode(stack[i])
            head = head.next

        return dummy.next






        

