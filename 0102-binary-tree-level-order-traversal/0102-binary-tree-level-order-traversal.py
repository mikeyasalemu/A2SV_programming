# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)
        self.helper(root,0)
        return list(self.dic.values())
    def helper(self,root,count):
        if root:
            self.dic[count].append(root.val)
            left = self.helper(root.left,count+1)
            right = self.helper(root.right,count+1)
      