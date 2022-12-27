class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hold =[]
#       give their ouble value to another list to check
        for index in arr:
            hold.append(index * 2)
            
        size = len(arr)
        
#       check if there is a value that satisfies the given formula 
        for num in range(size):
            if hold[num] in arr and num != arr.index(hold[num]) :
                return True
            
                
        return False