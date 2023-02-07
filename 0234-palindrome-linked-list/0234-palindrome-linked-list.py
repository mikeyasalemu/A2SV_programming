# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get list size
        size, cur = 0, head
        while cur:
            size, cur = size + 1, cur.next
        
        half = size // 2
       

        # rever half
        cur = None
        for i in range(half):
            tmp, head = head, head.next
            tmp.next = cur
            cur = tmp
        
        # advance one more if odd size
        if size & 1:
            head = head.next
        
        # check half
        for i in range(half):
            if cur.val != head.val:
                return False
            cur, head = cur.next, head.next
        return True
        