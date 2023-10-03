class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = [[costs[i][0] - costs[i][1], i] for i in range(len(costs))]
        
        arr.sort()
        
        ans = 0
        
        size = len(costs)
        for i in range(size):
            
            if i < size//2:
                ans += costs[arr[i][1]][0]
            else:
                ans += costs[arr[i][1]][1]
        
        return ans