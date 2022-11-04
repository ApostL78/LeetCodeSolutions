from typing import Optional
from problems.utils import ListNode, list2linkedlist, linkedlist2list
import pytest


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
         example: 1-->2-->3-->4-->5-->6-->7

         first step: head:1-->3-->4-->5-->6-->7, even_cp = 0-->2-->3-->....
                             ^
                           `cur`

        second step: head:1-->3-->5-->6-->7, even_cp = 0-->2-->4-->5...
                                  ^
        ....                    `cur`                         `even`
                                                                v
        after `while`: cur:1-->3-->5-->7, even_cp = 0-->2-->4-->6-->7
        """
        try:
            cur = head
            even = ListNode()
            even_cp = even
            while cur and cur.next:
                even.next = cur.next
                even = even.next
                cur.next = cur.next.next
                cur = cur.next if cur.next else cur  # `if` for lists, that has Even numbers of node
            even.next = None
            cur.next = even_cp.next

            return head
        except AttributeError:
            return head


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ([0], [0]),
    ([], []),
    ([-10 ** 6], [-10 ** 6]),
    ([10 ** 6], [10 ** 6]),
    ([-12345, 12345, 45324, 324324, 235, 23, 87, 2, 34, 34, 967, 2356, 790],
     [-12345, 45324, 235, 87, 34, 967, 790, 12345, 324324, 23, 2, 34, 2356]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 5, 7, 2, 4, 6, 8]),
    ([*range(10 ** 4 + 1)], [*range(0, 10001, 2)] + [*range(1, 10 ** 4, 2)]),
    ([13, 564, 869, -34, 124, 879, 2348, -4351, 672, 4577, 23215, -2, 12, -42],
     [13, 869, 124, 2348, 672, 23215, 12, 564, -34, 879, -4351, 4577, -2, -42]),
])
def test_odd_even_list(test_input, expected):
    solution = Solution()
    test_input = list2linkedlist(test_input)
    assert linkedlist2list(solution.oddEvenList(test_input)) == expected
