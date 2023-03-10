# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count =0
        self.helper(root,0,0)
        return self.count
    def helper(self,root,num,pre):
        if not root:
            return [num,pre]
        left = self.helper(root.left,num,pre)
        right = self.helper(root.right,num,pre)
        
        num+=left[0]+right[0]+1
        pre+= left[1]+right[1]+root.val
        if int(pre/num) == root.val:
            self.count+=1
        return [num,pre]
        