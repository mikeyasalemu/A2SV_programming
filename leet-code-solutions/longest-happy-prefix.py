class Solution:
    def longestPrefix(self, s: str) -> str:
        def kmp(pattern):
            m = len(pattern)
            # n = len(text)
            lsp = [0] * m
            j = 0
            
            for i in range(1,m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lsp[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                lsp[i] = j
            
            return lsp[-1]
        
        return s[:kmp(s)]