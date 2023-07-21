class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:        
        lesser = [0] * len(instructions)
        greater = [0] * len(instructions)
 
        def mergeSort(left, right, arr):
            if left >= right:
                return [[arr[left],left]]

            mid = left + (right - left)//2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid+1, right, arr)
            
            return merge(left_half, right_half)
        
        def merge(left_arr, right_arr):

            left = 0
            right = 0
            res = []
            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left][0] > right_arr[right][0]:
                    greater[right_arr[right][1]] += len(left_arr) -left
                    lesser[right_arr[right][1]] += left
                    res.append(right_arr[right])
                    right +=1

                elif left_arr[left][0] < right_arr[right][0]:
                    res.append(left_arr[left])
                    left+=1
                
                else:
                    idx = left
                    val = left_arr[left][0]

                    while left < len(left_arr) and right_arr[right][0] == left_arr[left][0]:
                        res.append(left_arr[left])
                        left += 1
                    while right < len(right_arr) and right_arr[right][0] == val:
                        greater[right_arr[right][1]] += len(left_arr)- left
                        lesser[right_arr[right][1]] += idx
                        res.append(right_arr[right])
                        right += 1





            while left < len(left_arr):
                res.append(left_arr[left])
                left += 1
        
            while right < len(right_arr):
                lesser[right_arr[right][1]] += left
                res.append(right_arr[right])
                right += 1 
                        
            return res

        lst = mergeSort(0 , len(instructions) -1, instructions)
        
        ans = 0
        
        for i in range(len(lesser)):
            ans+= min(lesser[i], greater[i])

        return  ans % (10**9 + 7)