# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        
        def traverse(node, arr):
            nonlocal targetSum
            if not node:
                return
            
            if not node.right and not node.left:
                arr = arr[:]+[node.val]
                if sum(arr) == targetSum:
                    self.ans.append(arr)
                return
            
            
            traverse(node.left, arr[:]+[node.val])
            
            traverse(node.right, arr[:]+[node.val])
        
        traverse(root, [])
        # print(self.ans)
        return self.ans