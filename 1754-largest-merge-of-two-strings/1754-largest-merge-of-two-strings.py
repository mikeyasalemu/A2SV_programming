class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        ans = ""
        while p1 < len(word1) and  p2 < len(word2):
                if word1[p1] > word2[p2]:
                    ans += word1[p1]
                    p1+=1
                    
                elif word1[p1] < word2[p2]:
                    ans += word2[p2]
                    p2+=1
                    
                else:
                    if word1[p1:] > word2[p2:]:
                        ans += word1[p1]
                        p1+=1
                    else:
                        ans += word2[p2]
                        p2+=1
                        
        while p1 < len(word1):
            ans+= word1[p1]
            p1+=1
        while p2 < len(word2):
            ans+= word2[p2]
            p2+=1
        
        return ans
                        
                    
            