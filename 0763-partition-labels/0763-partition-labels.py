class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic ={}
        ans = []
        for i in range(len(s)):
            dic[s[i]] = i
        last_idx = 0
        count = 0
        for i in range(len(s)):
            count+=1
            last_idx = max(dic[s[i]], last_idx)
            
            if i == last_idx:
                ans.append(count)
                count = 0
     
        return ans