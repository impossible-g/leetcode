# _*_coding:utf-8_*_
# __author: a123456
# Definition for a binary tree node.
from utils.utils import generate_tree_node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        r, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            r.append(node.val)
            root = node.right
        return r


if __name__ == '__main__':
    s = Solution()
    li = [1, None, 2, 3]
    node = generate_tree_node(li)
    print(s.inorderTraversal(root=node))
