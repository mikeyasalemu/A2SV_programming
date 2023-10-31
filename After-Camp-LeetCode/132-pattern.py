class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        low = float("inf")
        stack =[]
        for i in range(len(nums)):
            low = min(nums[i],low)
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            if stack and stack[-1][1] < stack[-1][0] > nums[i] and stack[-1][1] < nums[i]:
                return True
            stack.append([nums[i],low])
        return False
        