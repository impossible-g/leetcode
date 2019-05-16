# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        left = 0
        right = 0
        n = len(s)
        n1 = n + 1

        while right < n1 and left < n1:
            new_s = s[left:right]
            cur_s = s[right] if n != right else ''
            if cur_s in new_s:
                num = right - left
                if num > max_num:
                    max_num = num
                left += 1
            else:
                right += 1

        return max_num


if __name__ == '__main__':
    s = Solution()
    a = ' '
    print(s.lengthOfLongestSubstring(a))
