# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dic = defaultdict(int)
        self.dict = defaultdict(list)
        self.ans = 0
        self.helper(root,1,0)
        # print(self.dic)
        # print(self.dict)
        return self.ans
    def helper(self,root,count,level):
        # self.dic[count]+=1
        if not root: 
            return     
        # self.dict[count].append(self.dic[count])
        # self.ans = max(self.ans, (max(self.dict[count]) -min(self.dict[count])) +1)
        self.dict[level].append(count)
        self.ans = max(self.ans, (max(self.dict[level]) -min(self.dict[level])) +1)
        self.helper(root.left,(count*2) -1,level+1)
        self.helper(root.right,(count*2),level+1)
            