class Solution:
    def splitString(self, s: str) -> bool:
        self.check = False
        self.st = True
        s = s.lstrip("0")
        self.helper(0,s,"0","0")
        
        return self.check
    
    def helper(self,ind,s,prev,check):
        if not self.check:
            if int(prev) == 1 and  int(check) == 0:
                if ind+1 >= len(s):
                    self.check = True
                    return
                check+=s[ind+1]
                self.helper(ind+1,s,prev,check)
                return
            if int(prev) - int(check) == 1:
                prev = check
                if ind+1 >= len(s):
                    self.check = True
                    return
                check = s[ind+1]
                self.helper(ind+1,s,prev,check)
            elif int(prev) > int(check):
                if ind+1 >= len(s):
                    return
                check+=s[ind+1]
                self.helper(ind+1,s,prev,check)
                return
            elif  int(prev) < int(check) : 
                return
            for i in range(ind,len(s)-1):
                prev +=s[i]
                check = s[i+1]
                self.helper(i+1,s,prev,check)
            