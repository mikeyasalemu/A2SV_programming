# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        index = 0
        while head:
            while stack and stack[-1][0] < head.val:
                idx = stack.pop()[1]
                res[idx] = head.val
            stack.append([head.val, index])
            res.append(0)
            index += 1
            head = head.next
        return res