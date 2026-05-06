# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        print(stack)


        

        
        index = len(stack) - n
        if index == 0:
            return head.next if head else None
        current_idx = 0
        prev = None
        current = head

        

        while current and current_idx < index:
            prev = current
            current = current.next
            current_idx += 1
        

        if current:
            prev.next = current.next

        return head



        