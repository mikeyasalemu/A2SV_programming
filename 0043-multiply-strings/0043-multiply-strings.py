class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result1 = 0
        result2 = 0
        for nums1 in num1:
            result1 = 10* result1 + value[nums1]
        for nums2 in num2:
            result2 = 10* result2 + value[nums2]
        
        ret  = result1 * result2 
        
        return str(ret)