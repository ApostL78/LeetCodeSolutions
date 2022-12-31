import random
from typing import Optional, Tuple

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow, fast = head, head.next.next  # handling exception only few times
        except AttributeError:  # little faster
            return None  # instead of using "if" on every testcase

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


@pytest.fixture
def generate_input_and_expected_list(nodes: int) -> Tuple[
    Optional[ListNode], Optional[ListNode]]:
    mid = nodes // 2
    random_int = random.randint(1, 10 ** 5)
    input_list = ListNode(random_int)
    expected_list = ListNode(random_int)
    res = (input_list, expected_list)
    count = 1

    for _ in range(1, nodes):
        random_int = random.randint(1, 10 ** 5)
        if count == mid:
            count += 1
            input_list.next = ListNode(random_int)
            input_list = input_list.next
        else:
            count += 1
            input_list.next = ListNode(random_int)
            expected_list.next = ListNode(random_int)
            input_list = input_list.next
            expected_list = expected_list.next
    return res if expected_list.next else (input_list, None)


def linked_list_to_list(linked_list: Optional[ListNode]) -> list:
    res = []
    while linked_list:
        res.append(linked_list.val)
        linked_list = linked_list.next
    return res


@pytest.mark.parametrize("nodes", [7, 4, 2, 1, 10 ** 5, 12345, 8, 9, 987, 654])
def test_delete_middle(generate_input_and_expected_list, nodes):
    input_list, expected_list = generate_input_and_expected_list
    solution = Solution()
    assert linked_list_to_list(
        solution.deleteMiddle(input_list)) == linked_list_to_list(expected_list)
