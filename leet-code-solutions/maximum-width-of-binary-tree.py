# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dict = defaultdict(int)
        self.ans = 1
        self.helper(root,1,1)
        return self.ans
    def helper(self,root,count,level):
        
        if not root: 
            return     
        if self.dict[level] > 0:
            self.ans = max(self.ans, abs(self.dict[level] - count) +1)
            # print(level, self.dict[level])
        else:
            self.dict[level] = count
            # print(level, self.dict[level])
        self.helper(root.left,(count*2) -1,level+1)
        self.helper(root.right,(count*2),level+1)
            