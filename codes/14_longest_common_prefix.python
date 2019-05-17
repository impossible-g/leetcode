# _*_coding:utf-8_*_
# __author: {a123456}
class Solution:
    # def longestCommonPrefix(self, strs: [str]) -> str:
    #     length = len(strs)
    #     ret_str = ''
    #     if length:
    #         one_str = strs[0]
    #         one_s = ret_str
    #
    #         right = 0
    #         while 1:
    #             flag = True
    #             len_flag = True
    #             for j in strs:
    #                 if not j.startswith(one_s) or not j:
    #                     flag = False
    #                     break
    #
    #                 if len(j) == len(one_s):
    #                     len_flag = False
    #
    #             if flag:
    #                 right += 1
    #
    #                 if not len_flag:
    #                     ret_str = one_str[:right - 1]
    #                     break
    #
    #                 one_s = one_str[:right]
    #             else:
    #                 r = right - 1
    #                 if r > 0:
    #                     ret_str = one_str[:r]
    #                 break
    #
    #     return ret_str

    def longestCommonPrefix(self, strs: [str]) -> str:
        s_list = []
        pre_s = ''
        i = 0
        s_len = len(strs)

        while 1:
            for s in strs:
                n = len(s)
                if n >= i:
                    s_list.append(s[:i])
                else:
                    break

            if len(s_list) != s_len or len(set(s_list)) != 1:
                break
            i += 1
            pre_s = s_list[0]
            s_list.clear()

        return pre_s

    # def longestCommonPrefix(self, strs: [str]) -> str:
    #     if not strs:
    #         return ''
    #
    #     str_dict = self.dict_tree(strs)
    #     return self.search_str(strs[0], str_dict)
    #
    # def search_str(self, s, str_dict):
    #     cur = str_dict
    #     if len(cur) != 1:
    #         return ''
    #
    #     for i, char in enumerate(s):
    #         if len(cur[char]) != 1:
    #             return s[:i + 1]
    #         else:
    #             cur = cur[char]
    #     return ''
    #
    # def dict_tree(self, strs):
    #     root = {}
    #     max_len = 0
    #
    #     for i in strs:
    #         if len(i) > max_len:
    #             max_len = len(i)
    #
    #     for s in strs:
    #         cur = root
    #
    #         s = list(s)
    #         if len(s) != max_len:
    #             s.extend([''] * (max_len-len(s)))
    #
    #         for char in list(s):
    #             if char not in cur:
    #                 cur[char] = {}
    #             cur = cur[char]
    #
    #     return root


if __name__ == '__main__':
    s = Solution()
    l = ["aa","a"]
    print(s.longestCommonPrefix(l))
