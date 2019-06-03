# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    """
    字母压栈，如果当前字母与栈顶元素相同则删除其本身，和栈顶元素，最后栈中数据即是我么所需字符
    """
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    S = "abbaca"
    print(s.removeDuplicates(S))
