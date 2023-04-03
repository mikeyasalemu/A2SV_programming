class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.helper(arr,0,"")
        return self.ans
    def helper(self, arr, ind, curr):
        self.ans = max(self.ans, len(curr))
        # print(self.ans,curr)
        for i in range(ind, len(arr)):
            temp = curr+arr[i]
            # print(temp)
            freq = Counter(temp)
            # print(freq)
            if len(freq) == (len(curr)+len(arr[i])):
                self.helper(arr, i+1, temp)