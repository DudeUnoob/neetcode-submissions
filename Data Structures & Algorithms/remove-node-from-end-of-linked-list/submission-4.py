# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        stack = []

        current = head

        while current:
            stack.append(current)
            current = current.next

        
        index = len(stack) - n
        current_index = 0
        prev = None

        current = head

        if index == 0:
            return head.next if head else None

        while current and current_index < index:
            prev = current
            current = current.next
            current_index += 1

        if current:
            prev.next = current.next

        return head
        




