class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        size = len(grid[0])
        first= list(accumulate(grid[0]))
        second= list(accumulate((grid[1][::-1])))[::-1]
        # minValue = float('inf')
        lst = []
                
        for i in range(size):
            lst.append(max((first[-1]-first[i]) , (second[0]-second[i])))

        return min(lst)