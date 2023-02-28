class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        check = ""
        left = 0
        right = 0
        ans = 0
        
        while right < len(arr) -1:
            if check == "":
                if arr[right] < arr[right +1]:
                    check = "l"
                elif arr[right] > arr[right +1]:
                    check = "g"
                else:
                    check = ""
                    ans = max(ans, right - left +1)
                    left = right +1
            elif check == "g" and arr[right] < arr[right +1]:
                check = "l"
            
            elif check == "l" and arr[right] > arr[right +1]:
                check = "g" 
            else:
                check = ""
            ans = max(ans, right - left +1)
            if check == "":
                if arr[right] == arr[right +1]:
                    left = right +1
                else:
                    left = right
                    right -=1

            right+=1
        if check != "":
            ans = max(ans, right - left+1)
        return ans