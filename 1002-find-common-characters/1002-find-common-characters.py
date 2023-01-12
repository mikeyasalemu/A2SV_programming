class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = {}
        for x in words[0]:
            count[x] = count.get(x, 0) + 1
            
        
        for x in count:
            for i in range(1,len(words)):
                if x in words[i]:
                    count[x] = min(count[x], words[i].count(x))
                    
                else:
                    count[x] = 0
                    break
        
        ans = []
        for k,v in count.items():
            ans += v * [k]
        return ans
    