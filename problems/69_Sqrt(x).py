import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right


@pytest.mark.parametrize("test_input,expected", [
    (4, 2),
    (8, 2),
    (0, 0),
    (9, 3),
    (1, 1),
    (2, 1),
    (225, 15),
    (1000, 31),
    (2 ** 31 - 1, 46_340),
    (123456789, 11_111)
])
def test_contains_duplicate(test_input, expected):
    solution = Solution()
    assert solution.mySqrt(test_input) == expected
