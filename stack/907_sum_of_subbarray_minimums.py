# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    def sumSubarrayMins(self, A: [int]) -> int:
        stack = []
        sum = 0
        A.insert(0, 0)
        A.append(0)
        for i in range(len(A)):
            while stack and A[i] < A[stack[-1]]:
                out = stack.pop(-1)
                # (out - stack[-1]) 统计当前数左边为最小的次数
                # (i - out) 统计当前数右边为最小的次数
                sum += (out - stack[-1]) * (i - out) * A[out]
            stack.append(i)
        return sum % (pow(10, 9) + 7)


if __name__ == '__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    print(s.sumSubarrayMins(A))
