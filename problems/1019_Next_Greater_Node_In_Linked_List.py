from typing import Optional, List

import pytest

from problems.utils import ListNode, list2linkedlist


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        example: [2,7,4,3,5]
        first iteration: answer: [0], queue: [[2,0]], pos 1
        second iteration: answer: [7,0], queue: [[7,1]], pos 2
        third iteration: answer: [7,0,0], queue: [[7,1], [4,2]], pos 3
        fourth iteration: answer: [7,0,0,0], queue: [[7,1], [4,2], [3,3]] pos 4
        last iteration: answer: [7,0,0,0,0] --> [7,0,0,5,0] --> [7,0,5,5,0]
        """
        from collections import deque
        answer = []
        queue = deque()
        pos = 0
        while head:
            answer.append(0)
            while queue and queue[-1][0] < head.val:
                answer[queue.pop()[-1]] = head.val
            queue.append([head.val, pos])
            pos += 1
            head = head.next
        return answer


@pytest.mark.parametrize("test_input,expected", [
    ([2, 1, 5], [5, 5, 0]),
    ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0]),
    ([123], [0]),
    ([1], [0]),
    ([10 ** 9], [0]),
    ([*range(1, 10 ** 4 + 1)], [*range(2, 10 ** 4 + 1)] + [0]),
    ([2, 7, 4, 3, 2, 3, 5], [7, 0, 5, 5, 3, 5, 0]),
    ([4, 3, 2, 1, 5], [5, 5, 5, 5, 0]),
    ([6, 5, 4, 3, 2, 1, 5, 6], [0, 6, 5, 5, 5, 5, 6, 0]),
    ([6, 5, 4, 3, 2, 1, 5], [0, 0, 5, 5, 5, 5, 0])
])
def test_next_larger_nodes(test_input, expected):
    solution = Solution()
    test_input = list2linkedlist(test_input)
    assert solution.nextLargerNodes(test_input) == expected
