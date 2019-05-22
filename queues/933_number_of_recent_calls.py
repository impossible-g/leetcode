# _*_coding:utf-8_*_
# __author: a123456
class RecentCounter1:

    def __init__(self):
        self._queue = []

    def ping(self, t: int) -> int:

        if self._queue:
            while self._queue and t - 3000 > self._queue[0]:
                self._queue.pop(0)

        self._queue.append(t)

        return len(self._queue)


obj = RecentCounter1()
ts = [1, 100, 3001, 3002]
ret = []
for t in ts:
    ret.append(obj.ping(t))

print(ret)
