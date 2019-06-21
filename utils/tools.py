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
    """单向链表"""

    def __init__(self, li: []):
        self.length = 0
        self.root = self.init_list(li)

    def __iter__(self):
        cur = self.root

        while cur:
            yield cur.val
            cur = cur.next

    def _get_cur_pre(self, index):
        cur = self.root
        pre = None

        i = 0
        while i < index:
            pre = cur
            cur = cur.next
            i += 1

        return cur, pre

    def init_list(self, li):
        self.length = 1
        root = Node(li[0])
        cur = root

        for val in li[1:]:
            self.length += 1
            node = Node(val)
            cur.next = node
            cur = cur.next

        return root

    def is_empty(self):
        return self.root is None

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
        cur = self.root

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        self.root = pre


class DLinkList:
    """循环链表"""

    def __init__(self, li):
        self.length = 0
        self.root = self.init_list(li)
        self.iter_reverse = 0

    def __iter__(self):
        cur = self.root if not self.iter_reverse else self.root.prev

        i = 0
        while i < len(self):
            i += 1
            yield cur.val
            cur = cur.next if not self.iter_reverse else cur.prev

    def __contains__(self, item):
        flag = False
        cur = self.root
        i = 0

        while i < len(self):
            if cur.val == item:
                flag = True
                break
            cur = self.root.next

        return flag

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        cur = self.root

        i = 0
        while i < index:
            cur = cur.next
            i += 1

        return cur

    def __bool__(self):
        return self.root is None

    def _get_cur_pre(self, index):
        cur = self.root
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
        root = Node(li[0])
        cur = root
        pre = None

        for val in li[1:]:
            self.length += 1

            node = Node(val)
            cur.prev = pre
            cur.next = node
            pre = cur
            cur = cur.next

        cur.next = root
        cur.prev = pre
        root.prev = cur
        return root

    def insert(self, index, val):
        if index == 0:
            self.add(val)
            return

        cur, pre = self._get_cur_pre(index)

        self._init_new_node(val, pre, cur)

    def add(self, val):
        cur = self.root
        pre = self.root.prev

        self.root = self._init_new_node(val, pre, cur)

    def append(self, val):
        cur = self.root
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


class TrieNode:
    """字典树"""

    def __init__(self):
        self.nodes = {}

    def __contains__(self, word: str):
        """判断字符串在不在字典树中"""
        cur_map = self.nodes
        result = True

        for char in word:
            if char in cur_map:
                cur_map = cur_map[char]
            else:
                result = False
                break

        if "" not in cur_map:
            result = False

        return result

    def insert(self, word: str):
        cur_map = self.nodes

        for char in word:
            if char not in cur_map:
                cur_map[char] = {}
            cur_map = cur_map[char]

        cur_map[""] = ""

    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)

    @staticmethod
    def test():
        t = TrieNode()
        t.insert("abc")
        print("ab" in t)
        t.insert("ab")
        print("ab" in t)
        return t


class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        return (index - 1) >> 1

    def swap(self, index1, index2):
        self.data_list[index1], self.data_list[index2] = self.data_list[index2], self.data_list[index1]

    def insert(self, value):
        self.data_list.append(value)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)

        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def rm_max(self):
        rm_value = self.data_list[0]
        self.data_list[0] = self.data_list[1]
        del self.data_list[-1]

        self.heapify(0)
        return rm_value

    def heapify(self, index):
        total_index = len(self.data_list) - 1

        while 1:
            max_value_index = index

            n1 = 2 * index + 1
            if n1 <= total_index and self.data_list[n1] > self.data_list[max_value_index]:
                max_value_index = n1

            n2 = 2 * index + 2
            if n2 <= total_index and self.data_list[n2] > self.data_list[max_value_index]:
                max_value_index = n2

            if max_value_index == index:
                break

            self.swap(index, max_value_index)
            index = max_value_index

    @classmethod
    def test(cls):
        heap = cls()
        a = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
        for i in a:
            heap.insert(i)
        heap.rm_max()
        print(heap.data_list)


if __name__ == '__main__':
    TrieNode.test()
    Heap.test()
