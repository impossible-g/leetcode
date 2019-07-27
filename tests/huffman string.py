# _*_coding:utf-8_*_
# __author: a123456
from utils.utils import TreeNode


class HuffManTree:
    @classmethod
    def initialize_weight_list(cls, s):
        """初始化权值队列"""
        count_map = {}

        for char in s:
            count_map.setdefault(char, 0)
            count_map[char] += 1

        queue = sorted(list(count_map.items()), key=lambda x: x[1])
        return queue

    @classmethod
    def queue_add(cls, node, weight, queue):
        """添加时按顺序排好"""
        data = (node, weight)
        if not queue:
            queue.append(data)
        else:
            if weight <= queue[0][1]:
                queue.insert(0, data)
            elif weight >= queue[len(queue) - 1][1]:
                queue.append(data)
            else:
                # 排序
                for i, data in enumerate(queue):
                    if weight >= data[1]:
                        break
                queue.insert(i + 1, data)

    @classmethod
    def queue_get(cls, queue):
        return queue.pop(0)

    @classmethod
    def generate_queue(cls, weight_list):
        queue = []
        for val, weight in weight_list:
            node = TreeNode(val)
            node.left = None
            node.right = None
            cls.queue_add(node, weight, queue)

        return queue

    @classmethod
    def generate_tree(cls, queue):
        while len(queue) > 1:
            node = TreeNode(None)
            node.left = cls.queue_get(queue)
            node.right = cls.queue_get(queue)

            cls.queue_add(node, node.left[1] + node.right[1], queue)

        return queue[0]

    @classmethod
    def main(cls, s):
        weight_list = cls.initialize_weight_list(s)
        queue = cls.generate_queue(weight_list)
        tree = cls.generate_tree(queue)
        return tree


q = HuffManTree.main("abca")
print(q)
