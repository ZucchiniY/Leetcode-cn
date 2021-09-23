"""
先计算出正数的位置，注意 n = l - n -1，另外需要确认当 l = n 时，只移除第一个，也就是 curr = curr.next。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr, l = head, 0
        index = 0
        while curr:
            curr = curr.next
            l += 1

        curr = head
        if l == n:
            curr = curr.next
            return curr

        while index < l - n - 1:
            curr = curr.next
            index += 1

        curr.next = curr.next.next
        return head


"""
定义两个指针，s, e ，e指针指向 head 点，s 指向 ListNode(-1, head)

e 先移动 n 次，然后 s 和 e 同时移动，当 e 移动到尾部时，s 刚好移动到倒数第 n + 1 的位置。

将 s.next 指向 s.next.next 。

注意需要判断是否指向尾节点，如果是则返回 head 指针，如果不是返回 slow.next——因为 slow 是 (-1, head)
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, end = ListNode(-1, head), head
        for i in range(n):
            end = end.next
        flag = False
        while end:
            end = end.next
            slow = slow.next
            # 如果直接是尾结点的话，则不需要指向任务位置
            flag = True
        slow.next = slow.next.next
        return slow.next if not flag else head
