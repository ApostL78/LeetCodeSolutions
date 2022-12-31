import random
from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        slow algorithm but same as in graphical example.
        For faster algorithm check task #148 in problems.
        """
        sentinel = ListNode(-5001)
        while head:
            nxt = head.next
            head.next = None
            sentinel = self.insert_node(sentinel, head)
            head = nxt
        return sentinel.next

    def insert_node(self, head: Optional[ListNode], node: Optional[ListNode]) \
            -> Optional[ListNode]:
        cur = head
        while cur.next:
            if cur.val >= node.val:
                cur.val, node.val = node.val, cur.val
                cur.next, node.next = node, cur.next
                break
            cur = cur.next
        if not cur.next and cur.val <= node.val:
            cur.next = node
        elif cur.val > node.val:
            cur.val, node.val = node.val, cur.val
            cur.next, node.next = node, cur.next
        return head


@pytest.mark.parametrize("linked_list,expected", [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
    ([-1, 5, 3, 4, 0, 7], [-1, 0, 3, 4, 5, 7]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([-5000], [-5000]),
    ([1, 2], [1, 2]),
    ([5000, -5000], [-5000, 5000]),
    ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]),
    (random.sample(range(5000), 5000), [*range(5000)])
])
def test_insertion_sort_list(linked_list, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.insertionSortList(linked_list)
    assert linkedlist2list(res) == expected
