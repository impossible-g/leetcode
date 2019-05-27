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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# li = [1, None, 2, 3]
def generate_tree_node(li):
    node = TreeNode(li[0])
    cur_node = node
    for i in range(1, len(li)):
        if i % 2 == 1:
            cur_node.left = TreeNode(li[i])
        else:
            cur_node.right = TreeNode(li[i])
            cur_node = cur_node.right

    return node
