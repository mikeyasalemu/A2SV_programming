class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        default = image[sr][sc]
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        def dfs(row, col):
             if image[row][col] != default:
                    return
             image[row][col] = color
             visited.add((row, col))
             count = 0
             for row_change, col_change in directions:
                 new_row = row + row_change
                 new_col = col + col_change
                 if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
                    
             return 
            
             
        for i in range(len(image)):
            for j in range(len(image[0])):
                if i == sr and sc == j:
                    dfs(i,j)
        # print(image)
        return image