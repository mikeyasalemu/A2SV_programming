class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        max_length = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_length = max(max_length, count[s[right]])
            if right - left + 1 - max_length > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
                