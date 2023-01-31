class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)-1, 0, -1):
            if arr[i] != i+1:
                if arr.index(i+1) != 0:
                    ind = arr.index(i+1)
                    ans.append(ind+1)
                    arr = arr[ind::-1]+arr[ind+1:]
                    
                ans.append(i+1)
                arr = arr[i::-1]+arr[i+1:]
                    
              
        return ans
                    