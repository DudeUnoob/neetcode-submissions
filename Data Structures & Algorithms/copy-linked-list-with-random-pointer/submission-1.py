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
        
        clones = { None: None }

        curr = head

        while curr:
            copyNode = Node(curr.val)
            clones[curr] = copyNode
            print(curr.random)
            curr = curr.next

        
        curr = head

        while curr:

            clonedNode = clones[curr]
            clonedNode.next = clones[curr.next]
            clonedNode.random = clones[curr.random]
            curr = curr.next

        return clones[head]
            