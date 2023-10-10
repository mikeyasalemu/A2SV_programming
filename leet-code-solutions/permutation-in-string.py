class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        dic2 = defaultdict(int)
        dic1 = Counter(s1)
        if len(s1) > len(s2):
            return False
        for i in range(right):
            dic2[s2[i]] +=1
        if dic1 == dic2:
            return True
        while right < len(s2):
            dic2[s2[right]] += 1
            dic2[s2[left]] -= 1
            if dic2[s2[left]] == 0:
                dic2.pop(s2[left])
            right+=1 
            left+=1
            if dic1 == dic2:
                return True
        return False