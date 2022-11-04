from typing import List
import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for j in range(len(strs[0])):
            for i in range(len(strs) - 1):
                if len(strs[i + 1]) < j + 1:
                    return res
                if strs[i][j] == strs[i + 1][j]:
                    continue
                else:
                    return res
            res += strs[0][j]
        return res


@pytest.mark.parametrize("test_input,expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    ([""], ""),
    (["dog"], "dog"),
    (["veryLongTextveryLongTextveryLongTextveryLongTxtveryLongText", ""], ""),
    (["objectifying", "objectifying", "objectifying"], "objectifying"),
    (["dog", "racecar", "car", ""], ""),
    (["just", "justification", "justify"], "just"),
    (["dog", "door", "doom"], "do"),
    (["iterator", "italic", "item"], "it")
])
def test_longest_common_prefix(test_input, expected):
    solution = Solution()
    assert solution.longestCommonPrefix(test_input) == expected
