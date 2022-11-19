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


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def list2nodes(input_list: list[list]) -> Optional[Node]:
    if input_list:
        head = cur = Node(input_list[0][0])
        nodes = {0: head, None: None}

        for index in range(1, len(input_list)):
            cur.next = Node(input_list[index][0])
            nodes[index] = cur.next
            cur = cur.next

        cur = head
        for node in input_list:
            cur.random = nodes[node[1]]
            cur = cur.next
    else:
        head = None
    return head


def nodes2list(head: Optional[Node]) -> list[list]:
    output, nodes, index, cur = [], {None: None}, 0, head
    while cur:
        nodes[cur] = index
        index += 1
        cur = cur.next

    while head:
        output.append([head.val, nodes[head.random]])
        head = head.next
    return output
