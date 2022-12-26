class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        size = len(words)
        ret = True
        for i in range(26):
            dic[order[i]] = i
            
        hold = "" 
        for index , word in enumerate(words):
            hold = ""
            for ch in word:
                hold += chr(97 + dic.get(ch))
            words[index] = hold
        print (words)
         
        for index in range(size -1):
            if words[index] > words[index +1]:
                ret = False
                
        return ret
        