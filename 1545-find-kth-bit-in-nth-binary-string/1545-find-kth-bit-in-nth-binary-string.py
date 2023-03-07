class Solution:
    def findKthBit(self, n: int, k: int,f= -1) -> str:
        if n == 1:
            return "0"
        s = self.findKthBit(n -1,k,1)
        if f > 0:
            return s + "1" + self.invert(s)[::-1]
        else:
            return (s + "1" + self.invert(s)[::-1])[k-1]

        
    def invert(self,string):
        s = ""
        for i in string:
            if i == "1":
                s+= "0"
            else:
                s+= '1'
        return s