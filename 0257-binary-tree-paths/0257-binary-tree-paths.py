# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        self.helper(root,arr,"")
        return arr
    def helper(self,root,arr,s):
        if not root:
            return
        if s == "":
            s+= str(root.val)
        else:
            s+=  "->" + str(root.val)  
         
        if not root.right and not root.left:
            arr.append(s)
            return 
        elif root:
            self.helper(root.left,arr,s)
            self.helper(root.right,arr,s)
            return 
       
        
        