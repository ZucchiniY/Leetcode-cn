"""
第一个解法，先计算出长度，然后做一次循环计算出中间值。
"""


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next

        curr = ListNode()
        h = head
        for _ in range(0, l // 2):
            h = h.next

        curr = h
        return curr


"""
快慢指针法，慢指针走一步，快指针走两步，当fast 和 fast.next都存在时，继续走，如果不存在，则停止，慢指针刚好起到中间位置。
注意需要先判断是否为空链表。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
