# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        check = 0
        ans = ListNode(0)
        start = ans
        rem = 0
        while l1 or l2 or rem > 0:
            num = l1.val + l2.val + rem
            rem = 0
            if num > 9:
                rem = 1
                num -= 10
            ans.val = num
            if not l1.next and not l2.next and rem == 0:
                break
            else:
                temp = ListNode(0)
                ans.next = temp
                ans = ans.next
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0
            
        return  start
    