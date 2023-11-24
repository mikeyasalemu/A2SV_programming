# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        check = False

        if not head:
            return False

        fast = head.next
        
        while head and fast and fast.next:
            if head == fast:
                check = True
                break
            head = head.next
            fast = fast.next.next
        
        return check