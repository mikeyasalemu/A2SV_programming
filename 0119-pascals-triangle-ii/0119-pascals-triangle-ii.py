class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        arr= [1] * (rowIndex + 1)
        ret = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            arr[i] = ret [i -1] + ret [i]
        return arr
        