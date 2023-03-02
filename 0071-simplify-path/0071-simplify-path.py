class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []
        # print(path)
        for i in range(len(path)):
            if path[i] == "":
                if not ans or ans[-1]!='/':
                    ans.append('/')
            elif path[i] == "..":
                    if ans:
                        while ans and ans[-1] == "/" and len(ans) > 2:
                                  ans.pop()
                        if ans and len(ans) > 1:
                            ans.pop()
            elif path[i] == '.':
                 continue
            else:
                 ans.append(path[i])
                 ans.append('/')  
        while len(ans) > 2 and ans[-1] == '/':
            ans.pop()
            
        return "".join(ans)