class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block = False
        size = len(source)
        hold = ""
        temp = ""
        ans = []
        for  index  in range(size):
            
            temp = source[index]
            # print (temp, len(temp))
            itr = 0
            while itr < len(temp):
                if itr < len(temp) -1 and temp[itr] == '/' and temp[itr+1] == '*' and block == False:
                    block = True
                    itr +=1
                elif itr <len(temp) -1 and temp[itr] == '*' and  temp[itr + 1] == "/"and block == True:
                    block = False
                    itr +=1
                elif itr <len(temp) -1 and temp[itr] == '/' and  temp[itr + 1] == "/" and block == False:
                    break
                elif block == False:
                    hold += temp[itr]
                itr += 1
            if block == False and hold:
                ans.append(hold)
                hold = ""
        return ans