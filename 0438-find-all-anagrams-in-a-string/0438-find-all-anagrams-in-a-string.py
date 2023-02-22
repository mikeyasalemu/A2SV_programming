class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        dic = Counter(p)
        dic2 = defaultdict(int)
        ans = []
        if len(p) > len(s):
            return []
        while right < len(p):
            if dic2[s[right]]:
                dic2[s[right]] +=1
            else:
                dic2[s[right]] =1
            right +=1
                
        if dic == dic2:
            ans.append(left)
            
        while right < len(s):
            
            if dic2[s[left]] > 0:
               dic2[s[left]] -=1
            if dic2[s[left]] == 0:
               dic2.pop(s[left])
            left +=1
            dic2[s[right]] +=1
            
            if dic == dic2:
                ans.append(left)
            
            right+=1
        return ans