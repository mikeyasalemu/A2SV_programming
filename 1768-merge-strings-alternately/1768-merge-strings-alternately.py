class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = max(len(word1), len(word2))
        len1 = len(word1)
        len2 = len(word2)
        result = ""
        for x in range(size):
            if x < len1:
                result += word1[x]
            if x < len2:
                result += word2[x]
            if x >= len1 and x >= len2:
                break
        return result
                
                