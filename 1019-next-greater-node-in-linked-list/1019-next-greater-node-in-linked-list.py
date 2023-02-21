# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        start = head
        count = 0
        while head:
            head = head.next
            count +=1
        res = [0] * count
        
        index = 0
        while start:
            while stack and stack[-1][0] < start.val:
                idx = stack.pop()
                res[idx[1]] = start.val
            stack.append([start.val, index])
            index += 1
            start = start.next
        return res