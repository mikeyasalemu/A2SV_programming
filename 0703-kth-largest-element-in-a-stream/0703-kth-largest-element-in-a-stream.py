class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in nums:
            if len(self.nums) < k:
                heappush(self.nums,i)
            elif i > self.nums[0]:
                heappop(self.nums)
                heappush(self.nums,i)
                
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
                heappush(self.nums,val)
        elif val > self.nums[0]:
            heappop(self.nums)
            heappush(self.nums,val)
            
        return self.nums[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)