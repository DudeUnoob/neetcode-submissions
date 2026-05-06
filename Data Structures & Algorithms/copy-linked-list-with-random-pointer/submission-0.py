"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        oldCopy = {None: None}
        while curr:
            copy = Node(curr.val)

            oldCopy[curr] = copy

            curr = curr.next

        
        curr = head

        while curr:
            clone_node = oldCopy[curr]
            clone_node.next = oldCopy[curr.next]
            clone_node.random = oldCopy[curr.random]
            curr = curr.next

        return oldCopy[head]
