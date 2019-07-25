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


class Graph1:
    """无向图---> 邻接表实现"""

    def __init__(self):
        self.nodes = set()  # 图的点集
        self.edge = {}  # 图的边集

    def initialize_node(self, node):
        # 初始化点
        self.nodes.add(node)
        self.edge[node] = set()

    def insert(self, a, b):
        if a not in self.nodes: self.initialize_node(a)

        if b not in self.nodes: self.initialize_node(b)

        self.edge[a].add(b)
        self.edge[b].add(a)

    def succ(self, a):
        return self.edge[a]

    def show_nodes(self):
        print(self.nodes)

    def show_edge(self):
        print(self.edge)

    @classmethod
    def test(cls):
        graph = cls()
        graph.insert('0', '1')
        graph.insert('0', '2')
        graph.insert('0', '3')
        graph.insert('1', '3')
        graph.insert('2', '3')
        graph.show_edge()


class Graph2:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex)]

    def insert(self, a, b):
        self.graph[a - 1][b - 1] = 1
        self.graph[b - 1][a - 1] = 1

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print()

    @classmethod
    def test(cls):
        graph = cls(5)
        graph.insert(1, 4)
        graph.insert(4, 2)
        graph.insert(4, 5)
        graph.insert(2, 5)
        graph.insert(5, 3)
        graph.show()


def dfs(graph, start):
    """深度优先"""
    explored, stack = [start], [start]  # explored：已经遍历的节点列表，stack:寻找待遍历的节点栈

    while stack:
        v = stack.pop()

        # 遍历点
        for i in graph[v]:
            # 如果点不在已遍历列表，则遍历这个点
            if i not in explored:
                stack.append(i)
                explored.append(i)

    return explored


def bfs(graph, start):
    """广度优先"""
    explored, queue = [start], [start]  # explored：已经遍历的节点列表，stack:寻找待遍历的节点栈

    while queue:
        v = queue.pop(0)

        for i in graph[v]:
            if i not in explored:
                queue.append(i)
                explored.append(i)

    return explored


G = {'0': ['1'],
     '1': ['3'],
     '2': ['1'],
     '3': ['2', '4'],
     '4': ['5'],
     '5': ['7'],
     '6': ['4'],
     '7': ['6']}
if __name__ == '__main__':
    TrieNode.test()
    Heap.test()
    Graph1.test()
    Graph2.test()
    g = {'0': {'3', "1"}, '1': {'2', '0'}, '2': {'0', '3'}, '3': {'2', '1', '0'}}
    print(dfs(g, "0"))
    print(bfs(g, "0"))
