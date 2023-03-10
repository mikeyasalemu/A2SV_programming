# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dic = defaultdict(int)
        self.helper(root,0)
        for lst in sorted(self.dic):
            ans.append(self.dic[lst])
        # print(self.dic)
        return ans

    def helper(self,root,count):
        if not root:
            return

        self.helper(root.left,count+1)
        self.dic[count] = root.val
        self.helper(root.right,count+1)
        
      

        