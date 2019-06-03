# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        pre_num = nums[0]
        max_num = pre_num

        for i in range(1, len(nums)):

            cur_num = pre_num + nums[i]
            if cur_num > nums[i]:
                max_num = max(max_num, cur_num)
                pre_num = cur_num
            else:
                max_num = max(max_num, pre_num, cur_num, nums[i])
                pre_num = nums[i]

        return max_num


if __name__ == '__main__':
    s = Solution()
    nums = [8, -19, 5, -4, 20]
    print(s.maxSubArray(nums))
