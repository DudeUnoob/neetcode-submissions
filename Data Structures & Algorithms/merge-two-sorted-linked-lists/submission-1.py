class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:


        current = list1
        s1 = []

        while current:
            s1.append(current.val)

            current = current.next


        current2 = list2
        s2 = []

        while current2:
            s2.append(current2.val)
            current2 = current2.next
        

        s3 = s1 + s2

        s3.sort()

        dummy = ListNode()
        current = dummy


        for i in s3:
            #node val
            node = ListNode(i)
            current.next = node
            current = current.next

        return dummy.next
        
