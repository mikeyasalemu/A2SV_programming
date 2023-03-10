# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        self.helper(root)
        print(self.dic)
        lst = list(sorted(self.dic.values(), reverse = True))
        freq = lst[0]
        ans = []
        for key,val in self.dic.items():
            if val == freq:
                ans.append(key)
        return ans
    def helper(self,root):
        if not root:
            return 
        self.dic[root.val]+=1
        self.helper(root.left)
        self.helper(root.right)