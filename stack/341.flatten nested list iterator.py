# _*_coding:utf-8_*_
# __author: a123456
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    """
    如果当前容器有值，判断是列表还是数字
            数字 删除并返回
            列表 当前容器入栈，更新容器
        反之
            从栈中拿出上次的容器，并把第一项删除
    """

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.li = nestedList
        self.cur = self.li
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        if isinstance(self.cur[0], list):
            self.stack.append(self.cur)
            self.cur = self.cur[0]
            return self.next()
        elif isinstance(self.cur[0], int):
            result = self.cur.pop(0)
            while not self.cur and self.stack:
                self.cur = self.stack.pop()
                self.cur.pop(0)
            return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.li)


class NestedIterator(object):
    """
    """

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.li = self.dfs(nestedList)
        self.index = 0

    def dfs(self, li):
        nums = []
        for i in li:
            if isinstance(i, list):
                nums.extend(self.dfs(i))
            else:
                nums.append(i)

        return nums

    def next(self):
        """
        :rtype: int
        """
        ret = self.li[self.index]
        self.index += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index == len(self.li):
            return False
        return True


# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator([[1, 1], 2, [1, 1]]), []
while i.hasNext():
    v.append(i.next())

print(v)
