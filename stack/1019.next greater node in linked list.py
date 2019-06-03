# _*_coding:utf-8_*_
# __author: a123456
from utils.utils import ListNode, generate_list_node


class Solution:
    """
    遍历链表，把值和返回列表中的下标压栈，如果栈顶元素小于当前结点元素，
    则把返回列表中从上次下标到这次下标的值都改变为当前值
    """

    def nextLargerNodes(self, head: ListNode) -> [int]:
        stack = []
        results = []
        index = 0

        while head:
            results.append(0)
            val = head.val

            while stack and stack[-1][0] < val:
                results[stack.pop()[1]] = val

            stack.append([val, index])
            index += 1
            head = head.next

        return results

    # def nextLargerNodes(self, head: ListNode) -> [int]:
    #     if not head:  # 如果链表为空，直接返回空列表
    #         return []
    #     l = []  # 将链表的节点添加到列表中
    #     while head:
    #         l.append(head.val)
    #         head = head.next
    #     stack = []  # 定义一个空栈
    #     res = [0] * len(l)  # 定义一个长度与l相同，元素均为0的列表res, 如果扫描到更大节点则更新到res
    #     cnt = 0  # 列表下标初始化为0
    #     while cnt < len(l):  # 下标需要小于列表长度
    #         if not stack or l[stack[-1]] >= l[cnt]:  # 如果栈为空或者当前元素比栈顶对应元素小
    #             stack.append(cnt)  # 把当前下标压入栈
    #         else:
    #             while stack and l[stack[-1]] < l[cnt]:  # 如果栈不为空并且当前元素比栈顶对应元素大
    #                 res[stack[-1]] = l[cnt]  # 在res中更新与栈顶对应位置的元素
    #                 stack.pop()  # 把栈顶元素从栈中删除
    #             stack.append(cnt)  # 直到当前元素比栈顶对应元素小，再把当前下标压入栈
    #         cnt += 1  # 每次循环下标加1
    #     return res


if __name__ == '__main__':
    s = Solution()
    head = [1, 7, 5, 1, 9, 2, 5, 1]
    head = generate_list_node(head)
    print(s.nextLargerNodes(head))
