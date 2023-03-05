class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s) 
        self.left = 0
        self.right = size -1
        s = self.helper(self.left, self.right, s) 
    def helper(self,left, right, arr) -> list:
        if left >= right:
            return arr
        arr[left], arr[right] = arr[right],arr[left]
        left +=1
        right -=1
        return self.helper(left ,right, arr)
            
