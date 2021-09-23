"""
1. 因为链表本身没有提供长度的计算，所以需要单独计算一次长度 leng。
2. 依据长度计算出每个链接的基本长度为多少 each = leng // k
3. 计算出哪几个需要在基本长度上 + 1，remain = leng % k
4. 声明存储新链表头位置的数组 res = [None] * k
4.0 重新找出链表头，然后进行循环 curr = head
4.1 先将链表头保存到数组中， res[0] = curr
4.2 计算循环，然后将链表循环放入 for _ in range(i_len): last, curr = curr, curr.next 
4.3 到长度后，截断链表然后保存当前位置 last.next = None
5. 向第二段链表存入数据 index += 1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        p, n = head, 0
        # 计算链表长度
        while p != None:
            n += 1
            p = p.next

        # 几个链表需要长度 + 1
        add_count = n % k
        # 默认链表长度
        basic_len = n // k
        # 链表个数
        res = [None] * k

        curr = head
        index = 0
        while curr:
            # 记录 curr 开头
            res[index] = curr
            last = None

            i_len = basic_len + 1 if index < add_count else basic_len
            for i in range(i_len):
                last = curr
                curr = curr.next

            last.next = None
            index += 1

        return res
