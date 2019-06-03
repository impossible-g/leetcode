# _*_coding:utf-8_*_
# __author: {a123456}
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        n = 1

        while self.stack and price >= self.stack[-1][0]:
            _, num = self.stack.pop()
            n += num

        self.stack.append([price, n])
        return n


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    s = StockSpanner()
    l = [100, 80, 60, 70, 60, 75, 85]
    for i in l:
        print(s.next(i))
