from typing import Optional

import pytest

from problems.utils import list2linkedlist, linkedlist2list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        example: [1,2,3,4]
        first iteration: 2-->1-->3-->4, relink = `1` (node)
        second iteration without `relink` looks like this: 2-->1-->3-->None
        because of that we need to relink `1` (node) to `4`(node)
        second iteration: 2-->1-->4-->3, relink = `3` (node)
        """
        try:
            cur = head
            head = head.next
            relink = 0
            while cur and cur.next:
                if relink:
                    relink.next = cur.next
                nxt = cur.next
                cur.next = cur.next.next
                nxt.next = cur
                relink = cur
                cur = cur.next
            return head if head is not None else cur
        except AttributeError:
            return head


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], []),
    ([1], [1]),
    ([100], [100]),
    ([1, 2], [2, 1]),
    ([0, 100], [100, 0]),
    ([*range(100)], [
        1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18,
        21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36,
        39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54,
        57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72,
        75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90,
        93, 92, 95, 94, 97, 96, 99, 98
    ]),
    ([15, 22, 73, 64, 90, 88, 12], [22, 15, 64, 73, 88, 90, 12]),
    ([6, 7, 3, 2, 6, 8, 3, 0, 5, 6, 8], [7, 6, 2, 3, 8, 6, 0, 3, 6, 5, 8]),
    ([99, 98, 97, 96, 95, 94, 93, 92], [98, 99, 96, 97, 94, 95, 92, 93]),
])
def test_swap_pairs(test_input, expected):
    solution = Solution()
    test_input = list2linkedlist(test_input)
    assert linkedlist2list(solution.swapPairs(test_input)) == expected
