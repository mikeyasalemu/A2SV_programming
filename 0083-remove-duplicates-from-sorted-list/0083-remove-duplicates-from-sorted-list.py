# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
      
        if not start:
            return head
        
        num = head.val
        while start.next:
            if start.next.val == num:
                if start.next.next:
                    start.next = start.next.next
                else:
                    start.next = None
                    break
            else:
                num = start.next.val
                if start.next:
                    start = start.next
                else:
                    break
            
        return head
            