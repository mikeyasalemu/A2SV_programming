class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        length = len(s)
        sets= set(s)
        ans = 0
        for ch in sets:
            diff = 0
            left = 0
            right = 0
            while right < length:
                 if ch != s[right]:
                        diff+=1
                 if diff <= k:
                    ans = max(ans, right - left +1)
                 else:
                    while left < right:
                        if s[left] != ch:
                            diff -= 1
                            left+=1
                            break
                        left+=1
                            
                 right +=1
        return ans
                