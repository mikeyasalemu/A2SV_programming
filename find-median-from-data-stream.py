class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []
    def addNum(self, num: int) -> None:
        if len(self.min) == len(self.max):
            heappush(self.max, -heappushpop(self.min, -num))
        else:
            heappush(self.min, -heappushpop(self.max, num))
    def findMedian(self) -> float:
        if len(self.min) == len(self.max):
            return (self.max[0] - self.min[0]) / 2.0
        else:
            return float(self.max[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()