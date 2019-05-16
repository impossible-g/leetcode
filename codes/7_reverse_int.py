# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def reverse(self, x: int) -> int:
        max_num = 2 ** 31 - 1
        min_num = -max_num - 1
        flag = True if x >= 0 else False

        if not flag:
            x = -x
        new_x = int(str(x)[::-1])
        new_x = new_x if min_num < new_x < max_num else 0

        if not flag:
            new_x = -new_x
        return new_x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-210))
