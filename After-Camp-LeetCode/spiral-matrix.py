class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right = len(matrix[0])
        left = right -1
        down = len(matrix) -1
        up = down -1
        count = 0
        hold = "Right"
        ans = []
        row = 0
        column = 0
        for i in range(len(matrix)* len(matrix[0])):
            if hold == "Right":
                ans.append(matrix[row][column])
                count+=1
                if count == right:
                    hold = "Down"
                    right -=2
                    count = 0
                    row+=1
                else:
                    column+=1
            elif hold == "Down":
                ans.append(matrix[row][column])
                count+=1
                if count == down:
                    hold = "Left"
                    down -=2
                    count = 0
                    column-=1
                else:
                    row+=1
            elif hold == "Left":
                ans.append(matrix[row][column])
                count+=1
                if count == left:
                    hold = "Up"
                    left -=2
                    count = 0
                    row-=1
                else:
                    column-=1
            elif hold == "Up":
                ans.append(matrix[row][column])
                count+=1
                if count == up:
                    hold = "Right"
                    up -=2
                    count = 0
                    column+=1
                else:
                    row-=1
                
        return ans