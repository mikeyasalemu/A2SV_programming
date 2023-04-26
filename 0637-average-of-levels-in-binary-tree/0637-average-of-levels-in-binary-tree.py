# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.ans = []
        self.bfs([root])
        # print(self.ans)
        return self.ans
    
    def bfs(self,nodes):
        childs = []
        add = 0
        size = len(nodes)
        
        for node in nodes:
            add+= node.val
            if node.right:
                childs.append(node.right)
            if node.left:
                childs.append(node.left)
        self.ans.append(add/size)
        if childs:
            self.bfs(childs)
        
        