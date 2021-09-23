# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
