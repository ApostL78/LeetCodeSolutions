from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        for i in range(1, k):
            left = left.next

        left_cp = left
        while left_cp.next:
            right = right.next
            left_cp = left_cp.next
        left.val, right.val = right.val, left.val
        return head


@pytest.mark.parametrize("test_input,k,expected", [
    ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
    ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
    ([1], 1, [1]),
    ([0], 1, [0]),
    ([100], 1, [100]),
    ([12, 19, 45, 32, 35, 23, 87, 2, 34, 87, 96, 56, 90], 13,
     [90, 19, 45, 32, 35, 23, 87, 2, 34, 87, 96, 56, 12]),
    ([12, 19, 45, 32, 35, 23, 87, 2, 34, 87, 96, 56, 90], 1,
     [90, 19, 45, 32, 35, 23, 87, 2, 34, 87, 96, 56, 12]),
    ([*range(10 ** 5)], 1, [10 ** 5 - 1] + [*range(1, 10 ** 5 - 1)] + [0]),
    ([12, 19, 45, 32, 35, 23, 87, 2], 4, [12, 19, 45, 35, 32, 23, 87, 2]),
    ([12, 19, 45, 32, 35, 23, 87, 2, 4], 4, [12, 19, 45, 23, 35, 32, 87, 2, 4])
])
def test_swap_nodes(test_input, k, expected):
    solution = Solution()
    test_input = list2linkedlist(test_input)
    assert linkedlist2list(solution.swapNodes(test_input, k)) == expected
