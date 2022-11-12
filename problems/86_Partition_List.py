from typing import Optional

from problems.utils import ListNode, list2linkedlist, linkedlist2list
import pytest


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        sentinel_left, sentinel_right = left, right

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        left.next, right.next = sentinel_right.next, None
        return sentinel_left.next


@pytest.mark.parametrize("linked_list,x,expected", [
    ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
    ([2, 1], 2, [1, 2]),
    ([], 0, []),
    ([-100], -100, [-100]),
    ([100], 100, [100]),
    ([*range(200)], 50, [*range(200)]),
    ([*range(99, -1, -1)] + [*range(100, 200)], 50,
     [*range(49, -1, -1)] + [*range(99, 49, -1)] + [*range(100, 200)]),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], 5, [3, 4, 2, 0, 2, 8, 6, 7, 8, 9]),
    ([8, 3, 6, 4, 2, 7, 0, 9, 2], -5, [8, 3, 6, 4, 2, 7, 0, 9, 2])
])
def test_partition(linked_list, x, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.partition(linked_list, x)
    assert linkedlist2list(res) == expected
