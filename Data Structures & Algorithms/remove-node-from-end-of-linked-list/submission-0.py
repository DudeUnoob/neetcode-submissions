# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #[1,3,4,5,6,7,8], n = 2
        #remove 7
        #7 - 2 = 5
        stack = []

        def traverse(head=head):

            current = head

            while current:
                stack.append(current.val)
                current = current.next
        
        traverse()

        def deleteAndTraverse(head, index=len(stack) - n):
            
            if index == 0:
                return head.next if head else None
            
            current = head
            prev = None
            current_index = 0
            
            while current and current_index < index:
                prev = current
                current = current.next
                current_index += 1
            
        
            if current:
                prev.next = current.next
            
            return head
        return deleteAndTraverse(head)