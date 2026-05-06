class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        n = len(stack)
        l, r = 0, n - 1
        res = []

        while l <= r:
            res.append(stack[l])
            l += 1
            if l <= r:
                res.append(stack[r])
                r -= 1

        current = head
        for val in res:
            current.val = val
            current = current.next
