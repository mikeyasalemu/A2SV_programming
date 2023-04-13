# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hold = ListNode(0,head)
        curr = hold.next
        
        while curr and curr.next:
            if curr.val > curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                valid = hold
                while temp.val > valid.next.val:
                    valid = valid.next
                temp.next = valid.next
                valid.next = temp
            else:
                curr = curr.next
            
        
        return hold.next
        