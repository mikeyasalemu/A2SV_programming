class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        
        size = len(nums)
        def compare(x,y):
            
            if (y+x >= x+y):
                return 1
            return -1
        
        nums = sorted(nums, key = cmp_to_key(compare))
             
        if nums[0] == "0":
            return "0"
                
        return "".join(nums)