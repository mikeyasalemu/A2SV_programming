class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        i = 0
        ans = []
        for itr in range(len(matrix)):
            ans+= matrix[itr]
        heapify(ans)
        temp = nsmallest(k,ans)
        
        # print(ans)
        return temp[-1]