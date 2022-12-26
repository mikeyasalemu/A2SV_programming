class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size  = len(arr)
        index = 0
        count = 0
        
#         count the occurrence of zero until find non zero number and 
#         when we find, insert the zos upto their occrrence
        while index < size:
            if arr[index] == 0:
                count +=1
            elif arr[index] != 0:
                for iterate in range(count):
                    arr.insert(index -1, 0)
                    arr.pop()
                index += count
                count = 0
                
            index +=1
       
            