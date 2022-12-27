class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hold =[]
        for index in arr:
            hold.append(index * 2)
            
        index = 0 
        size = len(arr)
        temp = 0
        for num in range(size):
           
            if hold[num] in arr and num != arr.index(hold[num]) :
                return True
            
                
        return False