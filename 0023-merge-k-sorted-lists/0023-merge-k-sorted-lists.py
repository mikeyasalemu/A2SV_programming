# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(ans ,(lists[i].val,i))
           
                
        ret = ListNode(None)
        check = ListNode(None)
        check.next = ret
        while ans:
            val , node = heappop(ans)
            temp = ListNode(val)
            ret.next = temp
            ret = ret.next
            
            if lists[node].next:
                lists[node] = lists[node].next
                heappush(ans,(lists[node].val, node))

        return check.next.next