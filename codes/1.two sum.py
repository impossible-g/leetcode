# _*_coding:utf-8_*_
# __author: a123456
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = self.init_nums(nums)

        index_1 = None
        index_2 = None

        for i, num in enumerate(nums):
            other_num = target - num
            try:
                index_1 = i
                index_2 = nums_dict[other_num]
                if index_1 == index_2:
                    continue
                break
            except KeyError as e:
                continue

        return [index_1, index_2]

    def init_nums(self, nums):
        return {v: i for i, v in enumerate(nums)}


if __name__ == '__main__':
    n = [3, 2, 4]
    t = 6
    s = Solution()
    print(s.twoSum(n, t))
