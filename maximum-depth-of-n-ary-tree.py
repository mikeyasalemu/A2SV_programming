"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        self.visited = set()
        self.helper(root,1)
        return self.ans
    def helper(self,root,count):
        if not root or root in self.visited:
            return
        self.visited.add(root)
        self.ans = max(self.ans,count)
        for child in root.children:
            self.helper(child,count+1)
        return