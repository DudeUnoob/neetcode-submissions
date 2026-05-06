# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        flat = []

        for i in lists:
            current = i

            while current:
                flat.append(current.val)
                current = current.next

        flat.sort()

        dummy = ListNode()

        current = dummy

        # [1, 1, 2, 3, 3, 4, 5, 6]

        for i in flat:
            current.next = ListNode(i)
            current = current.next

        return dummy.next