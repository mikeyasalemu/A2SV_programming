class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        size_1 = len(s)
        size_2 = len(spaces)
        index_2 = 0
        for index_1 in range(size_1):
            if index_2 < size_2 and index_1 == spaces[index_2]  :
                string += " "+ s[index_1]
                index_2 +=1
            else:
                string += s[index_1]
       
        
        return string