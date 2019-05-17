# _*_coding:utf-8_*_
# __author: a123456
def binary_chop(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        m = int((l + r) / 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return l
