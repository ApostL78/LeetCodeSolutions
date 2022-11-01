import random
from typing import Optional
from problems.utils import list2linkedlist, ListNode, node_val_exists
import pytest


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """
        if randint will be the index of linked list, then time will be O(k),
        where `k` is random integer.
        else time will be O(n + k) ~ O(n), where n is number of nodes.
        """
        import random

        head = self.head
        index = random.randint(0, 10 ** 4)
        length = 0
        while head and index:
            length += 1
            index -= 1
            head = head.next

        if head:
            return head.val
        else:
            head = self.head
            index = random.randint(0, length - 1)
            while index:
                index -= 1
                head = head.next
            return head.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

@pytest.mark.parametrize("test_input", [
    [1, 2, 3],
    [1],
    [-10 ** 4],
    [10 ** 4],
    [*range(1, 10 ** 4 + 1)],
    [2, 7, 4, 3, 2, 3, 5],
    [15, 22, 73, 64, 90, 88, 12],
    [99, 98, 97, 96, 95, 94, 93, 92],
    [random.randint(-10 ** 4, 10 ** 4) for x in range(10 ** 4)],
    [random.randint(-10 ** 2, 10 ** 2) for y in range(10 ** 2)]
])
def test_swap_pairs(test_input):
    test_input = list2linkedlist(test_input)
    solution = Solution(test_input)
    assert node_val_exists(test_input, solution.getRandom())
