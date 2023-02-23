class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dic = defaultdict(int)
        ans= 0
        while right < len(s):
            dic[s[right]] += 1
            if dic[s[right]] > 1:
                # print (s[right], right)
                while dic[s[right]] > 1:
                    dic[s[left]]-=1
                    left +=1
                # print (s[left], left)
            # print(s[left], s[right])
            ans = max(ans, right-left+1)
            right +=1
        return ans
        