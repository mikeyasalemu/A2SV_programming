class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        max_len = len(max(arr, key=lambda x: len(x)))
        size = len(arr)
        ans = []
        
        for i in range(max_len):
            
            string = ""
            for  j in range(size):
                if i >= len(arr[j]):
                    string += " "
                else:
                    string += arr[j][i]
              
            ans.append(string.rstrip(" "))
        return ans
                