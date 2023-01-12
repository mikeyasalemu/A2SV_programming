class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [''] * numRows
        # for i in range(numRows):
        #     ans.append([])
        ind = 0
        forward = True
        
        for i in range(len(s)):
            ans[ind]+= s[i]
            if forward:
                if ind < numRows-1:
                    ind +=1
                else:
                    forward =False
                    ind -= 1
            else:
                if ind > 0:
                    ind -= 1
                else:
                    forward = True
                    ind += 1
        # print (ans)
        # res =[]
        # for row in ans:
        #     res += row
            
        return "".join(ans)
        