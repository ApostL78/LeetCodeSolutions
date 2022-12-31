from typing import List, Optional

import pytest

from problems.utils import ListNode, list2linkedlist


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, head = head, head.next
        critical_points, index, min_dist = [], 0, 10 ** 5

        while head.next:
            if (head.val > prev.val and head.val > head.next.val) or (
                    head.val < prev.val and head.val < head.next.val):
                critical_points.append(index)
                if len(critical_points) >= 2:
                    min_dist = min(min_dist,
                                   critical_points[-1] - critical_points[-2])
            index += 1
            prev = head
            head = head.next

        if critical_points and min_dist != 10 ** 5:
            return [min_dist, critical_points[-1] - critical_points[0]]
        else:
            return [-1, -1]


@pytest.mark.parametrize("linked_list,expected", [
    ([3, 1], [-1, -1]),
    ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
    ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ([*range(10 ** 5)], [-1, -1]),
    ([1, 2], [-1, -1]),
    ([10 ** 5 - 1, 10 ** 4, 10 ** 5], [-1, -1]),
    ([1, 3, 2, 2, 3, 2, 2, 2, 7, 1], [3, 7]),
    ([1, 4, 3, 2, 3, 2, 5, 2, 7, 1], [1, 7]),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-1, -1]),
    ([15, 14, 13, 12, 11, 10, 6, 9, 1], [1, 1])
])
def test_nodes_between_critical_points(linked_list, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    res = solution.nodesBetweenCriticalPoints(linked_list)
    assert res == expected
