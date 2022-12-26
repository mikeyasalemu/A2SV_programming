class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        values = 0
        index = values + 1
        count = 0
#         check for array size equal to 1

        if size == 1 and nums[0] != val:
            return 1
        
# swap the numbers equal to val to the back of array using two pointer

        while index < size:
            
            if nums[values] == val and nums[index] != val:
                nums[values] = nums[index]
                nums[index] = val
                values +=1
                index +=1
     
            elif nums[values] == val and nums[index] == val:
                index +=1
            else:
                values +=1
                index +=1
                
#       count the numbers differen from val

        for number in nums:
            if number != val:
                count+=1
            else:
                break
                
        return count
        