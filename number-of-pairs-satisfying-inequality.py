class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        def mergeSort(left, right, arr,diff):
            if left >= right:
                return [arr[left]]

            mid = left + (right - left)//2

            left_half = mergeSort(left, mid, arr,diff)
            right_half = mergeSort(mid+1, right, arr,diff)

            calc(left_half,right_half,diff)
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

        #########################
        def calc(arr1,arr2,diff):
            
            nonlocal ans 
            temp = 0
            count = 0
            left = len(arr1) -1
            right = len(arr2) -1

            while left >= 0 and right  >= 0:
                while right  >= 0 and  arr1[left] <= (arr2[right]+diff):
                    count +=1
                    right-=1

                temp+= count
                left -=1 

            while left >=0:
                temp+=count
                left-=1

            # print("state",arr1,arr2, temp)   
            ans += temp

        arr = [0]*len(nums1)
        for i in range(len(nums1)):
            arr[i] = nums1[i] - nums2[i]
        # print(arr)
        lst = mergeSort(0 , len(nums1) -1, arr,diff)
        # print(ans)
        return  ans