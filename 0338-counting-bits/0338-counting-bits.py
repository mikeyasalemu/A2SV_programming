class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1,n+1):
            ans = 0
            temp = 1
            for j in range(17):
                curr = (i & temp)
                if curr > 0:
                    ans+=1 
                temp = temp<<1
            arr.append(ans)
        # print(ans)
        return arr