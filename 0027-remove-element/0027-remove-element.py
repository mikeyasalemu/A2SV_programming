class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        values = 0
        index = values + 1
        count = 0
        if size == 1 and nums[0] != val:
            return 1
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
        for number in nums:
            if number != val:
                count+=1
            else:
                break
        print(nums)       
        return count
        