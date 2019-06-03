# _*_coding:utf-8_*_
# __author: a123456
class MinStack:
    """
    最小栈:
        保存当前的值和当前这些值中最小的值
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li = []  # ['x_当前最小值']
        self.min = None  # 最小值

    def push(self, x: int) -> None:
        if self.min is None or self.min > x:
            t = f'{x}_{x}'
            self.min = x
        else:
            t = f'{x}_{self.min}'

        self.li.append(t)

    def pop(self) -> None:
        self.li.pop()

        self.min = int(self.li[-1].split('_')[1]) if self.li else None

    def top(self) -> int:
        return int(self.li[-1].split('_')[0])

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_1 = obj.getMin()
    obj.top()
    obj.pop()
    param_2 = obj.getMin()
    print(param_1, param_2)
