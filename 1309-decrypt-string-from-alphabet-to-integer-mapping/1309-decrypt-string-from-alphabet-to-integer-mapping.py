class Solution:
    def freqAlphabets(self, s: str) -> str:
        x = len(s)-1
        result = ""
        while x >= 0:
            hold = ""
            if s[x] == '#':
                hold = s[x -2]+ s[x-1]
                print (hold)
                x -= 3
            elif s[x] != '#':
                hold = s[x]
                x -= 1
                print(hold)
            result = chr(96 + int(hold)) + result
            # result = hold + result
        return result
            
                