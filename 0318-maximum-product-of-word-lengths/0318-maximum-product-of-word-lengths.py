class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp = 1
        st = [0 for i in range(len(words))]

        
        for i in range(len(words)):
            for ch in words[i]:
                temp =  1 << (ord(ch) - ord('a'))
                st[i] |= temp
               
        ans = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if st[i]&st[j] == 0 and (len(words[i])*len(words[j])) > ans:
                        ans = len(words[i])*len(words[j])                
        return ans