# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        ans1 = defaultdict(set)
        ans2 = defaultdict(set)
        
        
        def check(dic, node, val):
            if node and not node.right and not node.left:
                dic[val] = set()
            
            if node and node.left:
                dic[val].add(node.left.val)
                check(dic, node.left, node.left.val)
                
            if node and node.right:
                dic[val].add(node.right.val)
                check(dic, node.right, node.right.val)
        
        if root1:
            check(ans1, root1, root1.val)
        if root2:
            check(ans2, root2, root2.val)
        
        ret = True
        
        if len(ans1) != len(ans2):
            
            return False
        
        for key, val in ans1.items():
            
            if key not in ans2:
                ret = False
                break
            for itm in val:
                
                if itm not in ans2[key]:
                    ret = False
                    break
                    
            if not ret:
                break
        
        return ret