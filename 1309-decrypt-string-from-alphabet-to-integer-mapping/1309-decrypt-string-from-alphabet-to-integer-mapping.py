class Solution:
    def freqAlphabets(self, s: str) -> str:
        x = len(s)-1
        result = ""
        
        
        # iterate starting from the last chracter
        while x >= 0:
            hold = ""
            
           # if there is '#' get he two numbers after it 
            if s[x] == '#':
                hold = s[x -2]+ s[x-1]
                x -= 3
            elif s[x] != '#':
                hold = s[x]
                x -= 1
                
             # by changinthe strngs in hold to int get the given char by usng 
              # char method  
            result = chr(96 + int(hold)) + result
        return result
            
                