class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minn = float("inf")
        if len(strs) == 1:
            res += str(strs[0])
            return res
        
        for y in range(len(strs)):
            minn = min(minn, len(strs[y]))
            
        for i in range(minn):
            for x in range(len(strs)):
                if strs[0][i] != strs[x][i]:
                    return res;
            res +=  str(strs[0][i])
        return res
            