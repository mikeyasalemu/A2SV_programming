class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        ans = 0
        while self.arr and self.arr[-1][0] <= price:
            ans+= self.arr[-1][1]
            self.arr.pop()
        self.arr.append([price,ans+1])
        return ans+1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)