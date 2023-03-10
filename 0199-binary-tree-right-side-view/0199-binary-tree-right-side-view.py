# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        self.arr = []
        # self.dic = defaultdict(int)
        self.helper(root,0)
        # for lst in sorted(self.dic):
        #     ans.append(self.dic[lst])
        # print(self.arr)
        return self.arr

    def helper(self,root,count):
        if not root:
            return
        if len(self.arr) < count+1:
            self.arr.append(0)
        self.helper(root.left,count+1)
        # self.dic[count] = root.val
        self.arr[count] = root.val
        self.helper(root.right,count+1)
        
      

        