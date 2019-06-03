# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        s = s.upper()
        n = len(s)

        while i < n:
            if s[i] in self.left_dict:
                next_s = s[i + 1] if i + 1 < n else ''
                if next_s in self.left_dict[s[i]]:
                    num += -(self.roman_num[s[i]] * 2)

            num += self.roman_num[s[i]]
            i += 1

        return num

    @property
    def left_dict(self):
        temp = {
            'I': {'V', 'X'},
            'X': {'L', 'C'},
            'C': {'D', 'M'},
        }
        return temp

    @property
    def roman_num(self):
        temp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("cm"))
