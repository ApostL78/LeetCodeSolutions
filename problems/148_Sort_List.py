from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        slow, fast = self.sortList(head), self.sortList(fast)

        return self.merge(slow, fast)

    def merge(self, left, right):
        sentinel = cur = ListNode()
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right
        return sentinel.next


# faster way (O(n)) but with O(n) memory usage:
# def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# vals = []
# cur = head
# while cur:
#     vals.append(cur.val)
#     cur = cur.next
# vals = sorted(vals)
# cur = head
# for val in vals:
#     cur.val = val
#     cur = cur.next
# return head

@pytest.mark.parametrize("linked_list,expected", [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
    ([], []),
    ([-10 ** 5], [-10 ** 5]),
    ([10 ** 5], [10 ** 5]),
    ([*range(5 * 10 ** 4)], [*range(5 * 10 ** 4)]),
    ([*range(5 * 10 ** 4 - 1, -1, -1)], [*range(5 * 10 ** 4)]),
    ([*range(5 * 10 ** 4 - 1)] + [-10 ** 5],
     [-10 ** 5] + [*range(5 * 10 ** 4 - 1)]),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], [0, 2, 2, 3, 4, 6, 7, 8, 8, 9])
])
def test_sort_list(linked_list, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.sortList(linked_list)
    assert linkedlist2list(res) == expected
