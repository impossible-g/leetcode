# _*_coding:utf-8_*_
# __author: {a123456}
from utils.utils import generate_list_node, ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_l1 = l1
        cur_l2 = l2
        new_l = ListNode(0)
        cur_new = new_l

        while cur_l1 or cur_l2:
            val1 = cur_l1.val if cur_l1 else None
            val2 = cur_l2.val if cur_l2 else None

            if val1 is not None and val2 is not None:
                if val1 <= val2:
                    cur_new.next = ListNode(val1)
                    cur_l1 = cur_l1.next
                else:
                    cur_new.next = ListNode(val2)
                    cur_l2 = cur_l2.next
            elif val1 is not None:
                cur_new.next = ListNode(val1)
                cur_l1 = cur_l1.next
            elif val2 is not None:
                cur_new.next = ListNode(val2)
                cur_l2 = cur_l2.next

            cur_new = cur_new.next

        return new_l.next


if __name__ == '__main__':
    s = Solution()
    l1 = []
    l2 = [0]
    l1 = generate_list_node(l1)
    l2 = generate_list_node(l2)
    a = s.mergeTwoLists(l1, l2)
    print(a)
