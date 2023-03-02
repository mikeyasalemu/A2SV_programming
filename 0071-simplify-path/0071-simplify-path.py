class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []
        # print(path)
        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                    if ans:
                        ans.pop()
            elif path[i] == '.':
                 continue
            else:
                 ans.append(path[i]) 
        ret = '/'.join(ans)
        ret = '/' + ret
        return ret