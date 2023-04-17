# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.helper(root,targetSum,[])
        return self.count
    def helper(self,root,target,arr):
        if not root:
            return 0
        arr.append(root.val)
        left = self.helper(root.left,target,arr)
        right = self.helper(root.right,target,arr)
        
        temp = 0
        for i in range(len(arr)-1,-1,-1):
            temp+= arr[i]
            if temp == target:
                self.count +=1
                
        arr.pop()
        return 0