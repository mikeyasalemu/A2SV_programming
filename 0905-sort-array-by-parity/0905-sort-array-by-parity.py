class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret = []
        for value in nums:
            if value % 2 == 0:
                ret.insert(0, value)
            else:
                ret.append(value)
        return ret
                
                