# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for i in range(len(lists)):
            while lists[i]:
                heappush(ans,lists[i].val)
                lists[i] = lists[i].next
                
        ret = ListNode(None)
        check = ListNode(None)
        check.next = ret
        while ans:
            temp = ListNode(heappop(ans))
            ret.next = temp
            ret = ret.next
        # print(check.next.next)
        return check.next.next