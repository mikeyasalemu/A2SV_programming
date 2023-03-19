# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)
        self.row = 0
        self.col = 0
        self.helper(root,0,0)
        sorted_dic = sorted(self.dic)
        result = []
        for key in sorted_dic:
            temp = sorted(self.dic[key])
            current = []
            for val in temp:
                current.append(val[1])
            result.append(current)
        return result
    def helper(self,root,row,col):
        if not root:
            return
        
        self.dic[col].append([row,root.val])
        self.helper(root.left,row+1,col-1)
        self.helper(root.right,row+1,col+1)
        