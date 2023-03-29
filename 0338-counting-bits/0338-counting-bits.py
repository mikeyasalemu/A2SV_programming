class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        print(3>>1)
        for i in range(n+1):
            curr = 0
            temp = i
            while temp >= 1:
                curr+= (temp&1)
                temp = temp>>1
                
            ans.append(curr)
        # print(ans)
        return ans