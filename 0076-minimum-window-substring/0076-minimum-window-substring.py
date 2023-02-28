class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        dic2 = defaultdict(int)
        if len(s) < len(t):
            return ""
        right = 0
        left = 0
        ans = float("inf")
        res = ""
        count = 0
        while right < len(s):
            dic2[s[right]] +=1
            if s[right] in dic and dic[s[right]] == dic2[s[right]]:
                    count+=1
            while count == len(dic):
                if right - left +1 < ans:
                     # print(s[right], s[left])
                     res = s[left: right +1]
                     ans = len(res)
                dic2[s[left]] -=1
                if s[left] in dic and dic2[s[left]] < dic[s[left]]:
                     count -=1
                left+=1

            right +=1
        return res
            