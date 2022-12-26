class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        size = len(words)
        ret = True
        
#       give the index of the order aphabet to dictionary
        for i in range(26):
            dic[order[i]] = i
#       replace the words by the value of their alphabet's index's
#          ascii character 
        hold = "" 
        for index , word in enumerate(words):
            hold = ""
            for ch in word:
                hold += chr(97 + dic.get(ch))
            words[index] = hold
         
#       check their order
        for index in range(size -1):
            if words[index] > words[index +1]:
                ret = False
                
        return ret
        