class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret = []
#         iterte throgh nums and append f not divisible by two 
#         and insert  at the left or first index if divible by two

        for value in nums:
            if value % 2 == 0:
                ret.insert(0, value)
            else:
                ret.append(value)
                
        return ret
                
                