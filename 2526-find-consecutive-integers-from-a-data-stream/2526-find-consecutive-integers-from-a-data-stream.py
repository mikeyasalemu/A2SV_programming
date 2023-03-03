class DataStream:

    def __init__(self, value: int, k: int):
        self.que = deque()
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num != self.value:
            self.que = []
        if len(self.que) >= self.k:
            return True
        return False
        # if len(self.que) < self.k:
        #     self.que.append(num)
        #     # print(self.que)
        #     if len(set(self.que)) == 1 and self.que[-1] == self.value and len(self.que) == self.k:
        #         return True
        #     return False
        # if len(self.que) == self.k:
        #     self.que[-1] = num
        #     if set(self.que) == 1 and self.que[-1] == self.value:
        #         return True
        #     return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)