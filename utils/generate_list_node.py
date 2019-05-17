# _*_coding:utf-8_*_
# __author: a123456
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_list_node(li):
    ln = None
    cur = None
    for i, v in enumerate(li):
        if not i:
            ln = ListNode(v)
            cur = ln
        else:
            cur.next = ListNode(v)
            cur = cur.next
    return ln
