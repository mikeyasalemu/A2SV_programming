class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        count = 0
#         Iterate through the numbers
        for num in nums:
            check = k - num
            
#             check holds the difference inorder to check if i present in the number list
            
            if dic[check] > 0 and dic[num] > 0 and check != num:
#             decreasing their value as we ave to delete the sums equal to k
#             for different numbers use different approach
                count += 1
                dic[check] -= 1
                dic[num] -= 1
            
            elif check == num and dic[check] > 1 :
#              if check and num are the same, use diefferent approach
                count +=1
                dic[check] -=2
        
        return  count 