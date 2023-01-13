class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for index in range(1, n+1):
            arr.append(index)
        hold = 0
        while len(arr) > 1:
            print(arr)
            hold += k -1
            if hold >= len(arr):
                hold = hold % len(arr)
            arr.pop(hold)
        return arr[0]
            