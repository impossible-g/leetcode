# _*_coding:utf-8_*_
# __author: a123456
from utils.utils import TreeNode, generate_tree_node


class BSTIterator:
    """
    中序遍历获得一个列表，每次取列表中的第一项
    """

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = self.ldr(root)

    def ldr(self, root):
        if not root:
            return []

        return self.ldr(root.left) + [root.val] + self.ldr(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)


if __name__ == '__main__':
    t = [7, 3, 15, 9, 20]
    tree = generate_tree_node(t)
    s = BSTIterator(tree)
