from typing import List

import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([1, 10, 39, 578, 27, -32, 4596], False),
    ([-99, -345, -1234, -99, 234, 23], True),
    ([1], False),
    ([*range(10 ** 5)], False),
    ([1 for _ in range(10 ** 5)], True),
    ([-10 ** 9], False),
    ([10 ** 9], False)
])
def test_contains_duplicate(test_input, expected):
    solution = Solution()
    assert solution.containsDuplicate(test_input) == expected
