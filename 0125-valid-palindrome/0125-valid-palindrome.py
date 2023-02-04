class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right =  len(s) -1
        check = True
        # print (ord('0'), ord('1'), ord('9')) 
        while left < right:
            if not s[left].isalpha() and not s[left].isnumeric():
                left += 1
            elif  not s[right].isalpha() and not s[right].isnumeric():
                right -=1
            else:
                if s[left] != s[right]:
                    check = False
                    break
                else:
                    
                    left +=1
                    right -=1
                    
        return check