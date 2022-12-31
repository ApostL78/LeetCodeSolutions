from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> \
            Optional[ListNode]:
        cur = head
        group_len = 2
        while cur and cur.next:
            n = 0
            prev = cur
            for _ in range(group_len):
                if cur.next:
                    cur = cur.next
                    n += 1
                else:
                    break
            if n % 2 == 0:
                prev.next, cur = self.reverse_k_nodes(prev.next, n)
            group_len += 1
        return head

    def reverse_k_nodes(self, head, k):
        """
        :return: first and last node of reversed list, so we can relink node
        before list
        """
        cur, prev, nxt = head.next, head, None
        while k - 1:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            k -= 1
        head.next = nxt
        return prev, head


@pytest.mark.parametrize("linked_list,expected", [
    ([5, 2, 6, 3, 9, 1, 7, 3, 8, 4], [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]),
    ([1, 1, 0, 6], [1, 0, 1, 6]),
    ([1, 1, 0, 6, 5], [1, 0, 1, 5, 6]),
    ([1, 5, 0, 2, 4, 7, 3, 6], [1, 0, 5, 2, 4, 7, 6, 3]),
    ([1 for _ in range(10 ** 5)], [1 for _ in range(10 ** 5)]),
    ([1], [1]),
    ([0], [0]),
    ([10 ** 5], [10 ** 5]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], [8, 6, 3, 4, 2, 7, 2, 9, 8, 0]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 2, 4, 5, 6, 7, 8, 9])
])
def test_sort_list(linked_list, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.reverseEvenLengthGroups(linked_list)
    assert linkedlist2list(res) == expected
