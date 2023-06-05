class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(left, right, arr):
            if left >= right:
                return [arr[left]]

            mid = left + (right - left)//2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid+1, right, arr)

            return merge(left_half, right_half)
        
        def merge(left_arr, right_arr):

            left = 0
            right = 0
            res = []
            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    res.append(left_arr[left])
                    left+=1
                else:
                    res.append(right_arr[right])
                    right+=1
            while left < len(left_arr):
                res.append(left_arr[left])
                left+=1 
            while right < len(right_arr):
                 res.append(right_arr[right])
                 right+=1 
            return res
  
        return  mergeSort(0 , len(nums) -1, nums)