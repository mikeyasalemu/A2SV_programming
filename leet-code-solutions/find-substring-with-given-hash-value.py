class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        res = deque()
        target = 0
        
        pw = 1
        for i in range(k):
            target += ((ord(s[i])- 96) * (pw)) 
            res.append(s[i])
            if i < k -1:
                pw *= power
            
        temp = target % modulo
        # print(47 % 20)
        if temp == hashValue:
            return "".join(res)
        
        for i in range(k,len(s)):
            res.popleft()
            
            target -= ord(s[i -k])- 96
            target //= power 
            
            target += ((ord(s[i])- 96) * pw)
            
            temp = target % modulo
            res.append(s[i])
            
            # print("".join(res), temp)
            if temp == hashValue:
                return "".join(res)
        
        return ""