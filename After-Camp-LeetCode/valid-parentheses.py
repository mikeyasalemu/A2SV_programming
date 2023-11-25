class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        
        for par in s:
            
            if par == '(':
                check.append(")")
            
            elif par == '{':
                check.append("}")
            
            elif par == '[':
                check.append("]")
            
            elif check and check[-1] == par:
                check.pop()
            else:
                return False
        
        return False if check else True