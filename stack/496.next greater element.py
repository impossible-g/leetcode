# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        mapping = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)

        return [mapping.get(num, -1) for num in nums1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3, 5, 2, 4]
    nums2 = [6, 5, 4, 3, 2, 1, 7]
    r = s.nextGreaterElement(nums1, nums2)
    print(r)
