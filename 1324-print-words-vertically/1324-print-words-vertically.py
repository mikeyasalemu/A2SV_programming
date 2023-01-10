class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        max_len = -math.inf
        size = len(arr)
        for i in range(size):
            max_len = max(max_len, len(arr[i]))
        ans = []
        for i in range(max_len):
            
            j =  0
            string = ""
            while j < size:
                if i > len(arr[j]) or i == len(arr[j]):
                    string += " "
                else:
                    string += arr[j][i]
                j+=1
            string = string.rstrip(" ")
            ans.append(string)
        return ans
                