from typing import Optional, List

import pytest

from problems.utils import ListNode, list2linkedlist, linkedlist2list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> \
            List[Optional[ListNode]]:
        output, length, cur = [], 0, head

        while cur:
            length += 1
            cur = cur.next

        """
        len of every part == length // k, but
        first k parts (where k == length % k) have part len + 1
        """
        while head:
            output.append(head)
            cur = head
            for _ in range(1, length // k):
                cur = cur.next
            if length % k and length // k:
                length -= 1
                cur = cur.next
            head = cur.next
            cur.next = None

        while len(output) != k:
            output.append(None)
        return output


@pytest.mark.parametrize("linked_list,k,expected", [
    ([1, 2, 3], 5, [[1], [2], [3], [], []]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ([], 10, [[], [], [], [], [], [], [], [], [], []]),
    ([], 1, [[]]),
    ([1000], 1, [[1000]]),
    ([*range(50)], 50, [[x] for x in range(50)]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], 5,
     [[8, 3], [6, 4], [2, 7], [0, 8], [9, 2]]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], 6,
     [[8, 3], [6, 4], [2, 7], [0, 8], [9], [2]]),
    ([8, 3, 6, 4, 2, 7, 0, 8, 9, 2], 11,
     [[8], [3], [6], [4], [2], [7], [0], [8], [9], [2], []]),
    ([*range(1000)], 2, [[*range(500)], [*range(500, 1000)]])
])
def test_split_list_to_parts(linked_list, k, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    output = solution.splitListToParts(linked_list, k)
    ans = []
    for i in range(len(output)):
        ans.append(linkedlist2list(output[i]))
    assert ans == expected
