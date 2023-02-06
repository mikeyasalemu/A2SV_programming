# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        hold = deepcopy(head)
        prev = None
        current = hold
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        rev = prev
        check = True
        if rev.val == None and head.val == None:
            return check
        else:
            p1 = rev
            p2 = head
            while p1 != None and p2 != None:

                if p1.val != p2.val:
                    check = False
                    break
                p1 = p1.next
                p2 = p2.next
                
        return check
        