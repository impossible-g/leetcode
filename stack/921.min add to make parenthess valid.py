# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    """
    把配对的括号给去掉，剩下的就是需要添加几个括号
    """
    def minAddToMakeValid(self, S: str) -> int:
        stack = []

        for char in S:
            if stack and stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


if __name__ == '__main__':
    s = Solution()
    S = "())"
    print(s.minAddToMakeValid(S))
