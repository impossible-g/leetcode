# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def calPoints(self, ops: [str]) -> int:
        sum_credit = 0
        stack = []
        for op in ops:
            if op in self.credit_map:
                sum_credit = self.credit_map[op](stack, sum_credit)
            else:
                sum_credit += int(op)
                stack.append(int(op))

        return sum_credit

    def add(self, stack, sum_credit):
        temp_credit = stack.pop()

        credit = temp_credit + stack[-1]
        sum_credit += credit

        stack.append(temp_credit)
        stack.append(credit)

        return sum_credit

    def d(self, stack, sum_credit):
        credit = stack[-1]
        credit = credit * 2
        stack.append(credit)
        sum_credit += credit
        return sum_credit

    def c(self, stack, sum_credit):
        credit = stack.pop()
        sum_credit -= credit
        return sum_credit

    @property
    def credit_map(self):
        temp = {
            "+": self.add,
            "D": self.d,
            "C": self.c
        }
        return temp


if __name__ == '__main__':
    a = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    s = Solution()
    print(s.calPoints(a))
