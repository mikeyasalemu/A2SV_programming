# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        temp = head
        while temp.next:
            count +=1
            if temp.next:
                temp =temp.next
            else:
                break
        dumy = ListNode(None)
        dumy.next = head
        head = dumy
        upto = count - n
        # print (upto)
        
        i = 0
        while i <= upto:
            if i == upto:
                if dumy.next and dumy.next.next:
                    dumy.next = dumy.next.next
                else:
                    dumy.next = None
                break
            else:
                dumy = dumy.next
                i+=1
        # print (dumy)
        return head.next
                