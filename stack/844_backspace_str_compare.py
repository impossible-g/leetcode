# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.get_new_str(S)
        t = self.get_new_str(T)
        return s == t

    def get_new_str(self, string: str) -> str:
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    S = "y#fo##f"
    T = "y#f#o##f"
    print(s.backspaceCompare(S, T))

