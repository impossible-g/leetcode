# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    """
    遍历序列pushed入栈，如果当前元素与popped的第一个元素相同则删除popped中第一个元素和栈顶元素，直至不等，
    继续压栈，最后判断栈中有没有有元素
    """
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        i = 0
        stack = []

        while i < len(pushed):
            stack.append(pushed[i])

            while stack and stack[-1] == popped[0]:
                popped.pop(0)
                stack.pop()

            i += 1

        return not bool(stack)


if __name__ == '__main__':
    s = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(s.validateStackSequences(pushed, popped))
