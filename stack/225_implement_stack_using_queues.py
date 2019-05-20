# _*_coding:utf-8_*_
# __author: a123456
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.li.append(x)
        # 反转队列
        i = 0
        while i < len(self.li) - 1:
            self.li.append(self.li.pop(0))
            i += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            return self.li.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.li[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.li)


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)
