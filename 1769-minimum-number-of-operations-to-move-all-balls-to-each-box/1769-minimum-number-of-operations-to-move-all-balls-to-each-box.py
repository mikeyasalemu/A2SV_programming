class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        size = len(boxes)
        right_dec = 0
        left_inc = 0
        right = 0
        left = 0
        for i in range(size):
            if boxes[i] == '1':
                right += i
                right_dec +=1
        
        for i in range(size):
            summ = 0
            summ = right + left
           
            if boxes[i] == '1':
                right_dec -= 1
                left_inc += 1
            right -= right_dec 
            left += left_inc
            ans.append(summ)
        return ans
            
        