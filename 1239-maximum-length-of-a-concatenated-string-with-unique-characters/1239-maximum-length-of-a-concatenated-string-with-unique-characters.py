class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.helper(arr,0,"")
        return self.ans
    def helper(self, arr, ind, curr):
        self.ans = max(self.ans, len(curr))
        for i in range(ind, len(arr)):
            temp = curr+arr[i]
            freq = Counter(temp)
            if len(freq) == (len(curr)+len(arr[i])):
                self.helper(arr, i+1, temp)