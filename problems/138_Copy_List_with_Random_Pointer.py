from typing import Optional

import pytest

from problems.utils import Node, list2nodes

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


@pytest.mark.parametrize("linked_list,expected", [
    ([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
     [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
    ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
    ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
    ([], []),
    ([[-10 ** 4, None]], [[-10 ** 4, None]]),
    ([[10 ** 4, None]], [[10 ** 4, None]]),
    ([[x, None] for x in range(1000)], [[x, None] for x in range(1000)]),
    ([[x, x] for x in range(1000)], [[x, x] for x in range(1000)]),
    ([[x, 0] for x in range(1000)], [[x, 0] for x in range(1000)]),
    ([[5, 1], [2, None], [6, 6], [3, 0], [9, 9], [1, 5], [7, 3], [3, 2],
      [8, None], [4, 4]],
     [[5, 1], [2, None], [6, 6], [3, 0], [9, 9], [1, 5], [7, 3], [3, 2],
      [8, None], [4, 4]])
])
def test_copy_random_list(linked_list, expected):
    solution = Solution()
    before = input_list = list2nodes(linked_list)
    after = solution.copyRandomList(input_list)
    while before and after and before.next and after.next:
        if before is after or before.next is after or (
                before.random is after.random and before.random is not None):
            assert False
        before, after = before.next, after.next
    assert (before is after is None) or (
            before is not after and before.random is not after)
