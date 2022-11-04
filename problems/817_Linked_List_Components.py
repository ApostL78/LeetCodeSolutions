import pytest
from typing import List, Optional
from problems.utils import ListNode, list2linkedlist


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        connected = 0
        nums = set(nums)  # comment this line for O(n^2) time and O(1) space
        while head:
            if head.val in nums:
                connected += 1
            else:
                if connected:
                    connected = 0
                    count += 1
            head = head.next

        return count if not connected else count + 1


@pytest.mark.parametrize("linked_list,nums,expected", [
    ([0, 1, 2, 3], [0, 1, 3], 2),
    ([0, 1, 2, 3], [0, 1, 2, 3], 1),
    ([0, 1, 2, 3, 4], [0, 3, 1, 4], 2),
    ([0, 1, 2, 3, 4, 5, 6], [2, 0, 3, 1, 4, 5], 1),
    ([0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 1, 4, 6], 3),
    ([0], [0], 1),
    ([1, 0], [0], 1),
    ([7, 5, 3, 1, 6, 2, 0, 4], [1], 1),
    ([7, 5, 3, 1, 6, 2, 0, 4], [1, 2, 3, 4], 3),
    ([*range(10 ** 4)], [*range(0, 10 ** 4, 2)], 10 ** 4 / 2)
])
def test_num_components(linked_list, nums, expected):
    solution = Solution()
    linked_list = list2linkedlist(linked_list)
    assert solution.numComponents(linked_list, nums) == expected
