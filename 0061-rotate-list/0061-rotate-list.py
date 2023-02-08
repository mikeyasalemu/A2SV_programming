# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        elif k == 0:
            return head
#         to know the length of out list
        temp = head
        size = 1
        while temp.next:
             temp = temp.next
             size+=1
            
            
        if  k == size:
            rot_val = k - size
        elif k > size:
            num = k // size
            rot_val = k -(num * size)
        else:
            rot_val = k
        
        if rot_val == 0:
            return head
#       to iterate upto the length thats going to be none
        start = head
        i = 1
        while i < size - rot_val:
            head = head.next
            i+=1
        hold = head.next
        hold_start = hold
        head.next = None

#         assign  the rest to another list
        while hold.next:
            hold = hold.next
        
#         add the rotated one to the original edited one
        hold.next = start
        head = hold_start
        
        return head
        # print(size//k , head)
        