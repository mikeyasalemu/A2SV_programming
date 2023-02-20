# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dumy = ListNode(0)
        dumy.next = head
        start = dumy
        while start.next and start.next.val < x:
            start  = start.next
        temp  = start
        
        while temp and temp.next:
            if temp.next.val < x:
                
                temp2 = ListNode(temp.next.val)
                temp3 = start.next
                start.next = temp2
                temp2.next = temp3
                start = start.next
                if temp.next.next:
                    temp.next =temp.next.next
                else:
                    temp.next = None
                
            
            else:
                temp = temp.next
        
        return dumy.next
                
         
                
                
                
        