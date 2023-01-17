class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
#        Insertion sort
        for i in range(size):
            val  = heights[i]
            val2 = names[i]
            j = i -1
            
            while j >= 0 and val > heights[j]:
                   
                names[j +1] = names[j]
                heights[j+1] = heights[j]
                j -=1
            names[j +1] = val2
            heights[j+1] = val
        return names