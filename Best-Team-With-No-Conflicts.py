class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = {}
        
        arr = [(ages[i], scores[i]) for i in range(len(ages))]
        
        arr.sort()
        
        for i in range(len(ages)):
            dp[i]  = arr[i][1]
            
         
        # print(arr)
        
        temp  = arr[0][1]
        for i in range(len(arr)):
            for j in range(i):
                
                if arr[j][1] <= arr[i][1]:
                    
                    dp[i] = max(dp[i], dp[j]+arr[i][1])
                
                temp = max(temp, dp[i])
        
        # print(dp)
        return temp
            
                
                
                
        