# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left: return head
        dummy = ListNode()
        dummy.next = head
        
        lists = dummy
        for i in range(1,left):
            lists = lists.next
        hold1 = lists
        temp = lists.next
        hold2 = temp
        node = None
        for i in range(right-left+1):
            newNode = temp
            temp = temp.next
            newNode.next = node
            node = newNode
        hold1.next = node  
        hold2.next = temp
        
        return dummy.next
            