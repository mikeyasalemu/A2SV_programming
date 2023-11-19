class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        
        sRev = nums2
        s = nums1
        
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        
        ans = 0
        for i in range(size1):
            for j in range(size2):
                if s[i] == sRev[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                    if dp[i][j] > ans:
                        ans = dp[i][j]
                        
                else:
                    dp[i][j] = 0
                
        
        # print(dp)
        
        return ans