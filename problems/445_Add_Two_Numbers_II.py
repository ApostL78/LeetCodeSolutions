from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
            Optional[ListNode]:
        integer_1, integer_2 = [], []
        while l1:
            integer_1.append(str(l1.val))
            l1 = l1.next

        while l2:
            integer_2.append(str(l2.val))
            l2 = l2.next

        result = str(int(''.join(integer_1)) + int(''.join(integer_2)))
        cur = ListNode()
        head = cur
        while result:
            cur.next = ListNode()
            cur = cur.next
            cur.val = int(result[0])
            result = result[1:]
        return head.next


@pytest.mark.parametrize("l1,l2,expected", [
    ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
    ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
    ([7, 2], [8, 1, 5, 9, 4], [8, 1, 6, 6, 6]),
    ([2, 1, 5], [5, 5, 0], [7, 6, 5]),
    ([9], [1], [1, 0]),
    ([0], [0], [0]),
    ([1 for _ in range(100)], [1 for _ in range(100)], [2 for _ in range(100)]),
    ([9 for _ in range(100)], [1], [1] + [0 for _ in range(100)]),
    ([9 for _ in range(100)], [9 for _ in range(100)],
     [1] + [9 for i in range(99)] + [8]),
    ([6, 5, 4, 3, 2, 1, 5, 6], [7, 0, 5, 5, 3, 5, 0], [7, 2, 4, 8, 7, 5, 0, 6])
])
def test_add_two_numbers(l1, l2, expected):
    solution = Solution()
    l1 = list2linkedlist(l1)
    l2 = list2linkedlist(l2)
    assert linkedlist2list(solution.addTwoNumbers(l1, l2)) == expected
