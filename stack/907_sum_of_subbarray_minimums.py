# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    """
    归纳法可以知道每个元素 A[i] 被加入到最终结果的次数为其左邻居中大于它、右邻居中不小于它的元素长度 left 、 right （包括自身）的乘积。
    """

    def sumSubarrayMins(self, A: [int]) -> int:
        stack = []
        ret = 0

        A.insert(0, 0)
        A.append(0)
        for i in range(len(A)):
            while stack and A[i] < A[stack[-1]]:
                out = stack.pop()
                left = out - stack[-1]
                right = i - out
                ret += A[out] * left * right

            stack.append(i)

        return ret % ((10 ** 9) + 7)


if __name__ == '__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    print(s.sumSubarrayMins(A))
