import pytest
from typing import Optional
from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> \
            Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        cur, length = head, 1
        while cur.next:
            length += 1
            cur = cur.next

        if not k % length:
            return head

        last = head
        for _ in range(length - k % length - 1):
            last = last.next

        new_head, last.next, cur.next = last.next, None, head

        return new_head


@pytest.mark.parametrize("linked_list,k,expected", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1]),
    ([], 0, []),
    ([-100], 1, [-100]),
    ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
    ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),
    ([100 for _ in range(500)], 1234, [100 for _ in range(500)]),
    ([*range(500)], 2 * 10 ** 9, [*range(500)])
])
def test_rotate_right(linked_list, k, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.rotateRight(linked_list, k)
    assert linkedlist2list(res) == expected
