class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_arr = []
        ans = []
        size = len(boxes)
        for i in range(size):
            if boxes[i] == '1':
                index_arr.append(i)
                
        size2 = len(index_arr)
        
        for i in range(size):
            summ = 0
            
            for j in range(size2):
                if i != index_arr[j]:
                    summ += abs(i - index_arr[j])
                
            ans.append(summ)
        return ans
            
        