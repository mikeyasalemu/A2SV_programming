class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.getScore(nums,0,len(nums)-1)
        if score >= 0:
            return True
        return False

    def getScore(self,arr,l,r):
        
        if l == r:
            ret = arr[l]
            return ret
        return max(arr[l] - self.getScore(arr, l +1, r), arr[r] - self.getScore(arr, l, r -1))
          
        
       