class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = -1
        size = len(arr)
        for i in range(size -1, -1,-1):
            temp = arr[i]
            arr[i] = last
            last = max(last, temp)
        return arr