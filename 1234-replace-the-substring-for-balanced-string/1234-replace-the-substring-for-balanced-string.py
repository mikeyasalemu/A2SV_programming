class Solution:
    def balancedString(self, s: str) -> int:
        dic = defaultdict(int)
        bal_val = len(s) // 4
        for i in range(len(s)):
            dic[s[i]] += 1
            # if dic[s[i]] > math.ceil(i/4) and i > 0:
            #     ans+= 1
        
        # print(len(dic))  
        for i in set(list(s)):
            if dic[i] <= (len(s)//4):
                del dic[i]
            else:
                dic[i] -= len(s)//4
        # print(dic)
        # print(sum(list(dic.values())))
        dic2 = defaultdict(int)
        if dic == dic2:
            return 0
        ans = float('inf')
        right = 0
        left = 0
        # print(dic)
        while right < len(s):
            if s[right] in dic:
                # print("yes")
                dic2[s[right]]+=1
                # print(" ",dic2,right,left)
            while left <= right and dic2['Q'] >= dic['Q'] and dic2['R'] >= dic['R'] and dic2['W'] >= dic['W'] and dic2['E'] >= dic['E']:
                ans = min(ans, right - left +1)
                # print(ans,dic2,right,left)
                if s[left] in dic2 and dic2[s[left]] > 0:
                    dic2[s[left]]-=1
                left+=1
            right+=1
        # print("END",ans) 
        return ans