class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = [0]*26
        for ch in words[0]:
            arr[ord(ch) -97] += 1

        size = len(words)
        for index in  range(1,size,1):
            arr2 = [0]*26
            for ch in words[index]:
                arr2[ord(ch) -97] += 1
            for itr in range(26):
                arr[itr] = min(arr[itr], arr2[itr])
                
        ans = []
        
        for index in range(26):
            ans += chr(index + 97) * arr[index]
        return ans
    