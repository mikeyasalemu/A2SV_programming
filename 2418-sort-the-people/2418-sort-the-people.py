class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        i = 0 
        j = 1
        while j < size -1:
            if  heights[i] > heights[j + 1]:
                break 
            elif j == size -1:
                return names
            j +=1
            i +=1
            
                
        for i in range(size):
            for j in range(size -1):
                if heights[j] < heights[j + 1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1],  heights[j]
       
        return names