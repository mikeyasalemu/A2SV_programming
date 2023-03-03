class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        extended_nums = nums + nums[:-1]
        # print (extended_nums)
        stack = []
        ans = [-1] * n
        for idx, num in enumerate(extended_nums):
            # print(idx, num)
            while stack and extended_nums[stack[-1]] < num:
                prev_idx = stack.pop()
                ans[prev_idx] = num
                
            if idx < n:
                stack.append(idx)
            # print (stack)
        
        return ans