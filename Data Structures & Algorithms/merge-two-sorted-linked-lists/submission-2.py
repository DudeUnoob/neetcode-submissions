# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1, stack2= [],[]

        head1 = list1
        head2 = list2

        while head1:
            stack1.append(head1.val)
            head1 = head1.next

        
        while head2:
            stack2.append(head2.val)
            head2 = head2.next

        stack3 = sorted(stack1 + stack2)

        dummy = ListNode()

        head = dummy

        for i in range(len(stack3)):
            head.next = ListNode(stack3[i])
            head = head.next

        return dummy.next

