class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        max_len = len(max(arr, key=lambda x: len(x)))
        size = len(arr)
        ans = []
        
        for i in range(max_len):
            
            j =  0
            string = ""
            while j < size:
                if i >= len(arr[j]):
                    string += " "
                else:
                    string += arr[j][i]
                j+=1
            string = string.rstrip(" ")
            ans.append(string)
        return ans
                