class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [''] * numRows
        # for i in range(numRows):
        #     ans.append([])
        if numRows == 1:
            return s
        ind = 0
        forward = True
        
        for i in range(len(s)):
            ans[ind]+= s[i]
            # print (ans)
            if ind == numRows -1:
                forward = False
            elif ind == 0:
                forward = True
            if forward:
                ind += 1
            else:
                ind -=1
            # if forward:
            #     if ind < numRows-1:
            #         ind +=1
            #     else:
            #         forward =False
            #         ind -= 1
            # else:
            #     if ind > 0:
            #         ind -= 1
            #     else:
            #         forward = True
            #         ind += 1
        # print (ans)
        # res =[]
        # for row in ans:
        #     res += row
            
        return "".join(ans)
        