class Heap:
    def __init__(self, li):
        self._values = li
        if li:
            self.build_heap()

    def is_empty(self):
        return not self._values

    # 取堆顶元素
    def peek(self):
        if self.is_empty():
            raise ValueError("堆为空")
        return self._values[0]

    # 上浮
    def siftup(self, value):
        last_index = len(self._values) - 1
        values, i, j = self._values, last_index, (last_index - 1) // 2

        while i > 0 and value < values[j]:
            values[i] = values[j]
            i, j = j, (j - 1) // 2

        values[i] = value

    # 插入
    def push(self, value):
        self._values.append(None)
        self.siftup(value)

    # 下沉
    def siftdown(self, value, index):
        values, index, i = self._values, index, index * 2 + 1
        max_index = len(values)

        while i < max_index:
            if i + 1 < max_index and values[i + 1] < values[i]:
                i += 1
            if value < values[i]:
                break
            values[index] = values[i]
            index = i
            i = 2 * i + 1
        values[index] = value

    # 弹出
    def pop(self):
        if self.is_empty():
            raise ValueError("堆为空")
        values = self._values
        e0 = values[0]
        e = values.pop()
        if len(values) > 0:
            self.siftdown(e, 0)
        return e0

    # 从数组构建堆
    def build_heap(self):
        for index in range(len(self._values) // 2 - 1, -1, -1):
            self.siftdown(self._values[index], index)


if __name__ == '__main__':
    a = Heap([10, 9, 6, 7, 8, 2, 5, 1, 4, 3])
    print(a)
