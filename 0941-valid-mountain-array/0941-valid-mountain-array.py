class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
            size = len(arr)
            if size < 3:
                return False
            inc = 0
            dec = size -1
            while inc < size -2 and arr[inc] < arr[inc + 1]:
                inc +=1
            while dec > 1 and arr[dec] < arr[dec -1]:
                dec -= 1
                
            # if dec == 0 or inc == size -1:
            #     return False
            return dec == inc