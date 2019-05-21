# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        primitive_list = []
        stack = []
        left = 0
        for right, char in enumerate(S):
            if char == "(":
                stack.append(char)
            else:
                stack.pop()

            if not stack:
                primitive_list.append(S[left + 1:right])
                left = right + 1

        return ''.join(primitive_list)


if __name__ == '__main__':
    s = Solution()
    S = "(()())(())(()(()))"
    print(s.removeOuterParentheses(S))
