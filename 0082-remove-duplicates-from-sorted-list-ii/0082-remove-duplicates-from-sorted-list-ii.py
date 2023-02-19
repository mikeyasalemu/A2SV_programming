# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dumy = ListNode(0)
        ans = dumy
        start = head
        num = start.val
        count = 0
        while start.next:
            if start.next.val == num:
                count = 1
            else:
                num = start.next.val
                if count == 0:
                    temp = ListNode(start.val)
                    dumy.next = temp
                    dumy = dumy.next
                count = 0
            start = start.next
        if count == 0:
            temp = ListNode(start.val)
            dumy.next = temp
        
        return ans.next
            