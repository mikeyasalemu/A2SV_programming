# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        odd = head
        ans = head
        size = 1
        while head and  head.next:
            head = head.next
            size +=1
        if size > 2:
            for i in range(int(size/2)):
                temp = ListNode(odd.next.val)
                # print(temp)
                odd.next = odd.next.next
                temp.next = None
                odd = odd.next

                head.next = temp
                # print (temp)
                head = head.next
                # print(ans)
                # print(head)
            
     
            
        return ans