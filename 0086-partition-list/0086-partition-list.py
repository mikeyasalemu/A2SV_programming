# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dumy = ListNode(0)
        dumy.next = head
        left = dumy
        while left.next and left.next.val < x:
            left  = left.next
        right  = left.next
        
        while right and right.next:
            if right.next.val < x:
                
                temp = ListNode(right.next.val)
                temp2 = left.next
                left.next = temp
                temp.next = temp2
                left = left.next
                if right.next.next:
                    right.next =right.next.next
                else:
                    right.next = None
                
            
            else:
                right = right.next
        
        return dumy.next
                
         
                
                
                
        