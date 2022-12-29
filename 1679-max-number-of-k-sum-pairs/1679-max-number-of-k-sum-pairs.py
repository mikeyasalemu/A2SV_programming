class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        print (dic)
        # nums.sort()
        print (nums)
        count = 0
        for num in nums:
            check = k - num
            if dic[check] > 0 and dic[num] > 0 and check != num:
                count += 1
                dic[check] -= 1
                dic[num] -= 1
            elif check == num and dic[check] > 1 :
                count +=1
                dic[check] -=2
                
            # if num != check:
            # dic[num] += 1 
        
        return  count 