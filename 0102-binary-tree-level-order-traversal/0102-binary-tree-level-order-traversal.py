# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self.helper(root,0,dic)
        return list(dic.values())
    def helper(self,root,count,dic):
        if root:
            dic[count].append(root.val)
            left = self.helper(root.left,count+1,dic)
            right = self.helper(root.right,count+1,dic)
      