class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
            ans = True
            inc = True
            for i in range(len(arr) -1):
                  if arr[i] == arr[i +1]:
                        ans = False
                        break
                  elif inc:
                    if arr[i] > arr[i+1]:
                        if i == 0:
                            return False
                        else:
                            inc = False
                        
                  else:
                    if arr[i] < arr[i +1]:
                        return False
            if inc:
                ans = False
            return ans