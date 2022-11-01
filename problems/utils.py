from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2linkedlist(input_list: list) -> Optional[ListNode]:
    if input_list:
        head = ListNode(input_list[0])
        current = head
        for val in input_list[1:]:
            current.next = ListNode(val)
            current = current.next
    else:
        head = None
    return head


def linkedlist2list(linked_list: Optional[ListNode]) -> list:
    res = []
    while linked_list:
        res.append(linked_list.val)
        linked_list = linked_list.next
    return res


def node_val_exists(head: Optional[ListNode], val: int) -> bool:
    while head:
        if val == head.val:
            return True
        head = head.next
    return False
