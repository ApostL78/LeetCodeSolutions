from typing import Optional

from problems.utils import Node

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
        try:
            new_head = cur = Node(head.val)
            first, nodes, head = head, {head: cur, None: None}, head.next

            while head:
                cur.next = Node(head.val)
                cur = cur.next
                nodes[head] = cur
                head = head.next
            cur.next = None

            cur = new_head
            while first:
                cur.random = nodes[first.random]
                cur, first = cur.next, first.next

            return new_head
        except AttributeError:
            return head
