# _*_coding:utf-8_*_
# __author: a123456
import random

from utils.tools import Node


class LinkList:
    """单循环链表"""

    def __init__(self, li=None):
        self.length = 0
        self.root = self.initialize(li)

    def initialize(self, li):
        if not li:
            return Node(None)

        top_node = Node(li[0])

        cur = top_node
        for ele in li[1:]:
            node = Node(ele)
            cur.next = node
            cur = node

        cur.next = top_node
        self.length = len(li)
        return cur

    @classmethod
    def generate(cls):
        _li = [i for i in range(1, 10)]
        random.shuffle(_li)
        l = cls(_li)
        cur = l.root
        data = []

        for i in range(len(_li)):

            start = cur.val
            temp = []
            while 1:
                cur = cur.next
                val = cur.val
                if val == start:
                    cur = cur.next
                    break

                temp.append(val)

            data.append(temp)

        random.shuffle(data)
        random.shuffle(data)
        random.shuffle(data)

        for i in data:
            [print(j if random.choice([2, 1, 0]) > 0 else " ", end="  ") for j in i]
            print()

        return data


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    LinkList.generate()
