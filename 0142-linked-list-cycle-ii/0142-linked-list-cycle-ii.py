# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        second_start = head
        i = 0
        while start and start.next:
            start = start.next.next
            head = head.next
            i +=1
            if head == start:
                while second_start and head:
                    if second_start == head:
                        return head
                    second_start = second_start.next
                    head = head.next
                
            
        return 
            