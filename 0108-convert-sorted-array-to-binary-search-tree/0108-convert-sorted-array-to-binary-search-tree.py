# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.helper(0,len(nums) -1)
    def helper(self,left,right):
        if left <= right:
            mid = left + (right - left) // 2
            ans = TreeNode(self.nums[mid], self.helper(left,mid -1), self.helper(mid +1,right))
            return ans
        # return ans