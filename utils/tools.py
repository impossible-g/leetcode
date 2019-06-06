# _*_coding:utf-8_*_
# __author: a123456
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, li: []):
        self.length = 0
        self.head = self.init_list(li)

    def __iter__(self):
        cur = self.head

        while cur:
            yield cur.val
            cur = cur.next

    def _get_cur_pre(self, index):
        cur = self.head
        pre = None

        i = 0
        while i < index:
            pre = cur
            cur = cur.next
            i += 1

        return cur, pre

    def init_list(self, li):
        self.length = 1
        head = Node(li[0])
        cur = head

        for val in li[1:]:
            self.length += 1
            node = Node(val)
            cur.next = node
            cur = cur.next

        return head

    def is_empty(self):
        return self.head is None

    def get_length(self):
        return self.length

    def insert(self, index, val):
        cur, pre = self._get_cur_pre(index)
        pre.next = Node(val)
        pre.next.next = cur

        self.length += 1

    def remove(self, index):
        cur, pre = self._get_cur_pre(index)
        pre.next = cur.next

        self.length -= 1

    def reverse(self):
        pre = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        self.head = pre



