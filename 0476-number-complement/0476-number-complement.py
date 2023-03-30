class Solution:
    def findComplement(self, num: int) -> int:
        temp = 0
        ans = 0
        # print(2<<0)
        count = 0
        while num > 0:
            if not num&1:
                temp+=1
                temp = temp << count
                ans+= temp
                temp = 0
            count+=1
            num = num>>1
        # print(ans)
        # print(ans)
        return ans