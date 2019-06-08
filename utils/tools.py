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


class DLinkList:
    def __init__(self, li):
        self.length = 0
        self.head = self.init_list(li)
        self.iter_reverse = 0

    def __iter__(self):
        cur = self.head if not self.iter_reverse else self.head.prev

        i = 0
        while i < len(self):
            i += 1
            yield cur.val
            cur = cur.next if not self.iter_reverse else cur.prev

    def __contains__(self, item):
        flag = False
        cur = self.head
        i = 0

        while i < len(self):
            if cur.val == item:
                flag = True
                break
            cur = self.head.next

        return flag

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        cur = self.head

        i = 0
        while i < index:
            cur = cur.next
            i += 1

        return cur

    def __bool__(self):
        return self.head is None

    def _get_cur_pre(self, index):
        cur = self.head
        pre = None

        i = 0
        while i < index:
            pre = cur
            cur = cur.next
            i += 1

        return cur, pre

    def _init_new_node(self, val, pre, cur):
        node = Node(val)
        node.prev = pre
        node.next = cur
        cur.prev = node
        pre.next = node

        self.length += 1
        return node

    def init_list(self, li):
        self.length = 1
        head = Node(li[0])
        cur = head
        pre = None

        for val in li[1:]:
            self.length += 1

            node = Node(val)
            cur.prev = pre
            cur.next = node
            pre = cur
            cur = cur.next

        cur.next = head
        cur.prev = pre
        head.prev = cur
        return head

    def insert(self, index, val):
        if index == 0:
            self.add(val)
            return

        cur, pre = self._get_cur_pre(index)

        self._init_new_node(val, pre, cur)

    def add(self, val):
        cur = self.head
        pre = self.head.prev

        self.head = self._init_new_node(val, pre, cur)

    def append(self, val):
        cur = self.head
        pre = cur.prev

        self._init_new_node(val, pre, cur)

    def pop(self, index):
        cur, pre = self._get_cur_pre(index)
        pre.next = cur.next
        cur.next.prev = pre

        cur.next = None
        cur.prev = None

        self.length -= 1
        return cur


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = DLinkList(nums)

    head.insert(0, 0)
    print(head[1].val)
    for i in range(3):
        a = hash('[1, "2", ]')
        print(a)
        a = hash('[1, "2" ]')
        print(a)
