class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        prefix = 0
        ans = 0
        satisfaction.sort(reverse = True)
        for i in satisfaction:
            
            prefix += i
            if prefix < 0:
                break
            ans += prefix 
            
        # ans = 0
        
        return ans
        