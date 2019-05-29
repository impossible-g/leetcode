# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    def oddEvenJumps(self, A: [int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    # 如果栈顶下标小于当前下标，则在返回列表中栈顶下标改为当前下标
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key=lambda i: A[i])  # 排序好的列表的下标
        odd_next = make(B)
        B.sort(key=lambda i: -A[i])  # 倒序B
        even_next = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if odd_next[i] is not None:
                odd[i] = even[odd_next[i]]
            if even_next[i] is not None:
                even[i] = odd[even_next[i]]

        return sum(odd)


if __name__ == '__main__':
    s = Solution()
    A = [10, 13, 12, 14, 15]
    print(s.oddEvenJumps(A))
