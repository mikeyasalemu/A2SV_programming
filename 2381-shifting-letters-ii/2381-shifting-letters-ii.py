class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        words = "abcdefghijklmnopqrstuvwxyz"
        words = list(words)
        lst = [0]*(len(s) +1)
        s =list(s)
        for left, right, check in shifts:
            if check == 0:
                x = -1
            else:
                x= 1
            lst[left] += x
            lst[right+1] += -1* x
        for i in range(1,len(lst)):
            lst[i] = lst[i] + lst[i -1]
       
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            index+= lst[i]
            s[i] = words[index%26]
        return "".join(s)