# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        right = len(needle)

        for i in range(len(haystack) - right + 1):
            if haystack[i: i + right] == needle:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack, needle))
