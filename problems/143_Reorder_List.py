from typing import Optional

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        reverse right half of list and then reorder it:
        input: 1->2->3->4
        1 step: 1->2<-3<-4
                   |
                  None
        2 step: sentinel->1->4->2->3->None
        3 step: head = sentinel 
        """
        slow, fast, prev = head, head.next, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        sentinel = ListNode()
        while head and prev != head:
            sentinel.next = head
            head = head.next
            sentinel = sentinel.next
            sentinel.next = prev
            prev = prev.next
            sentinel = sentinel.next
        if prev == head:
            sentinel.next = prev
        else:
            sentinel.next = None
        head = sentinel.next


@pytest.mark.parametrize("linked_list,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([1000], [1000]),
    ([1 for _ in range(5 * 10 ** 4)], [1 for _ in range(5 * 10 ** 4)]),
    ([5, 2, 6, 3, 9, 1, 7, 3, 8, 4], [5, 4, 2, 8, 6, 3, 3, 7, 9, 1]),
    ([1, 1, 0, 6], [1, 6, 1, 0]),
    ([1, 1, 0, 6, 5], [1, 5, 1, 6, 0])
])
def test_reorder_list(linked_list, expected):
    solution = Solution()
    input_list = list2linkedlist(linked_list)
    solution.reorderList(input_list)
    assert linkedlist2list(input_list) == expected
