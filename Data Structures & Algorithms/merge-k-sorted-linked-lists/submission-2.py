# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        stack = []

        for i in range(len(lists)):

            current = lists[i]

            current_list = []

            if not current:
                
                continue
            
            
            # iterate linked list on lists[i]

            while current:
                stack.append(current.val)
                current = current.next

            
        stack = sorted(stack)

        dummy = ListNode()
        head = dummy

        for i in range(len(stack)):
            head.next = ListNode(stack[i])
            head = head.next

        return dummy.next


