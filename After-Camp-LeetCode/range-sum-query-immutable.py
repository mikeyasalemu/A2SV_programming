class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]
        for i in range(len(nums)):
            self.presum.append(self.presum[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        self.ans = self.presum[right +1] - self.presum[left]
        return self.ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)