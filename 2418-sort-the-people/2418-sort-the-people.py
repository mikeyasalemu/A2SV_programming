class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
       
        for i in range(size):
            index = i
            for j in range(i +1, size):
                if heights[index] < heights[j]:
                    index = j
            if i != index:
                names[index], names[i] = names[i], names[index]
                heights[i], heights[index] = heights[index],  heights[i]
       
        return names