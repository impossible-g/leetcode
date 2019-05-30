# _*_coding:utf-8_*_
# __author: {a123456}
import heapq


class StockSpanner:
    """
    维护一个递减栈，如果当前值比栈顶大，则循环查找到下一个比当前值大的元素

    """

    def __init__(self):
        self.heap = []  # [[price, n]]

    def next(self, price: int) -> int:
        heapq.heappush(self.heap, price)
        print(self.heap)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    s = StockSpanner()
    l = [100, 80, 60, 70, 60, 75, 70]
    for i in l:
        print(s.next(i))
