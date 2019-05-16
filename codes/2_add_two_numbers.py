# _*_coding:utf-8_*_
# __author: a123456
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1, l2, n = self.pacth_li(l1, l2)

        new_l = None
        new_cp = None
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            two_sum = l1_val + l2_val + carry
            carry = 0
            if two_sum > 9:
                carry, two_sum = self.get_num(two_sum)

            if not new_l:
                new_l = ListNode(two_sum)
                new_cp = new_l
            else:
                new_cp.next = ListNode(two_sum)
                new_cp = new_cp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # return self.rev_li(new_l)
        # return self.split_li(new_l, n)
        return new_l

    def get_num(self, two_sum):
        a = two_sum // 10
        b = two_sum % 10
        return a, b

    def add_link(self, li, i, n):
        if i < n:
            i += 1
            if not li.next:
                li.next = ListNode(0)
            self.add_link(li.next, i, n)

    def pacth_li(self, l1, l2):
        """补位"""
        l1_num = l2_num = 1
        l1_cp, l2_cp = l1, l2
        while l2_cp.next or l1_cp.next:
            if l1_cp.next:
                l1_num += 1
                l1_cp = l1_cp.next

            if l2_cp.next:
                l2_num += 1
                l2_cp = l2_cp.next

        if l1_num > l2_num:
            n = l1_num
            big_li, small_li = l1, l2
        else:
            n = l2_num
            big_li, small_li = l2, l1

        i = 1
        self.add_link(small_li, i, n)

        return big_li, small_li, n

    def split_li(self, li, n):
        i = 0

        def inner(i, li):
            i += 1
            if i == n:
                li.next = None
                return
            inner(i, li.next)

        inner(i, li)
        return li

    def rev_li(self, li):
        """反转"""
        pre = li
        cur = li.next
        pre.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


def generate_list_node(li):
    ln = None
    cur = None
    for i, v in enumerate(li):
        if not i:
            ln = ListNode(v)
            cur = ln
        else:
            cur.next = ListNode(v)
            cur = cur.next
    return ln


def print_li(li):
    print(li.val, end='')
    if not li.next:
        return
    print_li(li.next)


if __name__ == '__main__':
    l1 = [9, 9, 9, 9, 9]
    l2 = [1]
    l1 = generate_list_node(l1)
    l2 = generate_list_node(l2)
    s = Solution().addTwoNumbers(l1, l2)
    print_li(s)
    print()
