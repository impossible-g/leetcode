# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = int((l + r) / 2)
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return l


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(s.searchInsert(nums, target))
