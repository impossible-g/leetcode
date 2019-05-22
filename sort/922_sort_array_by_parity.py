# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        """奇数位和偶数位互相交换， 相当与单次遍历"""
        i = 0
        j = 1
        len_a = len(A)

        while i < len_a and j < len_a:
            if A[i] % 2 == 0:
                i += 2
            else:
                while A[j] % 2 == 1 and j < len_a:
                    j += 2

                if j < len_a:
                    A[i], A[j] = A[j], A[i]
                    i += 2

        return A

    # def sortArrayByParityII(self, A: [int]) -> [int]:
    #     i = 0
    #
    #     while i < len(A):
    #
    #         if A[i] % 2 == 1:
    #             j = i - 1 if i > 1 else 1
    #
    #             while j < len(A):
    #                 if A[j] % 2 == 0:
    #                     A[j], A[i] = A[i], A[j]
    #                     break
    #                 j += 2
    #             else:
    #                 break
    #
    #         i += 2
    #
    #     return A


if __name__ == '__main__':
    s = Solution()
    a = [3, 0, 4, 0, 2, 1, 3, 1, 3, 4]

    print(s.sortArrayByParityII(a))
