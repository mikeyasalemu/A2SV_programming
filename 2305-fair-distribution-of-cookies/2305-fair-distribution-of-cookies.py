class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        st = [0]*k
        self.ans = sum(cookies)
        self.helper(cookies,k,st,0)
        return self.ans
    def helper(self,cookies,k,st,ind):
        if ind == len(cookies):
            self.ans = min(self.ans,max(st))
            return
        for i in range(k):
            if st[i]+ cookies[ind] < self.ans:
                st[i] += cookies[ind]
                self.helper(cookies,k,st,ind+1)
                st[i] -= cookies[ind]