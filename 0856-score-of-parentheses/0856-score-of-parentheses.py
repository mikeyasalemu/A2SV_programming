class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        ans = []
        
        for i in range(len(s)):
            if s[i] == '(':
                ans.append(s[i])
            else:
                temp = 1
                if not ans[-1] == '(':
                    temp = ans.pop() * 2
                ans.pop()
                if ans and not ans[-1] == '(':
                    ans[-1] += temp
                else:
                    ans.append(temp)
                
        
        return ans[-1]
                
        