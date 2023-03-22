class Solution:
    def balancedString(self, s: str) -> int:
        dic = defaultdict(int)
        bal_val = len(s) // 4
        for i in range(len(s)):
            dic[s[i]] += 1

        for i in set(list(s)):
            if dic[i] <= (len(s)//4):
                del dic[i]
            else:
                dic[i] -= len(s)//4

        dic2 = defaultdict(int)
        
        if dic == dic2:
            return 0
        
        ans = float('inf')
        right = 0
        left = 0
        while right < len(s):
            if s[right] in dic:
                dic2[s[right]]+=1
                
            while left <= right and dic2['Q'] >= dic['Q'] and dic2['R'] >= dic['R'] and dic2['W'] >= dic['W'] and dic2['E'] >= dic['E']:
                ans = min(ans, right - left +1)
                if s[left] in dic2 and dic2[s[left]] > 0:
                    dic2[s[left]]-=1
                left+=1
            right+=1
        return ans