# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flat = []
        for node in lists:
            while node:
                flat.append(node.val)
                node = node.next

        flat.sort()

        print(flat)

        res = ListNode(0)

        current = res

        for i in flat:
            current.next = ListNode(i)
            current = current.next

        return res.next
        
        
     