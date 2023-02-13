# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        if not list1 and not list2:
            return 
        start = ans
        while list1 and list2:
            if list1.val > list2.val:
                ans.val= list2.val
                list2 = list2.next
            else:
                ans.val= list1.val
                list1 = list1.next
            temp = ListNode(0)
            ans.next = temp
            ans = ans.next
        while list1:
            ans.val= list1.val
            list1 = list1.next
            if list1:
                temp = ListNode(0)
                ans.next = temp
                ans = ans.next
        while list2:
            ans.val= list2.val
            list2 = list2.next
            if list2:
                temp = ListNode(0)
                ans.next = temp
                ans = ans.next
        return start