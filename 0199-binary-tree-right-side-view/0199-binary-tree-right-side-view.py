# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dic = defaultdict(list)
        self.helper(root,ans,0)
        print(self.dic)
        for lst in sorted(self.dic):
            ans.append(self.dic[lst][-1])
        return ans

    def helper(self,root,ans,count):
        if not root:
            return
        # ans.append(root.val)
        # if root.right:
        self.helper(root.left,ans,count+1)
        self.helper(root.right,ans,count+1)
        self.dic[count].append(root.val)
        # ans.append(self.dic[count][-1])
        print(self.dic[count])

        