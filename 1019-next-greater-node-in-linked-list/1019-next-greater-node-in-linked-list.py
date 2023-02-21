# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        start = head
        index = 0
        while start:
            while stack and stack[-1][0] < start.val:
                idx = stack.pop()[1]
                res[idx] = start.val
            stack.append([start.val, index])
            res.append(0)
            index += 1
            start = start.next
        return res