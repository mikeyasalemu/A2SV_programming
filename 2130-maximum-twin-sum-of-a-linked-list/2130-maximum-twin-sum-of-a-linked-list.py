# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rev = head
        temp = head
        size = 1
        while temp:
            if temp.next.next:
                 temp = temp.next.next
                 rev = rev.next
            else:
                break
            size+=1
        cur = None
        while rev:
            tmp, rev = rev, rev.next
            tmp.next = cur
            cur = tmp
        maxx = 0
        i = 0
        while i <= size -1:
            maxx = max(cur.val+head.val , maxx)
            cur = cur.next
            head = head.next
            i = i+1
        return maxx