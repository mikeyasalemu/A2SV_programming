class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        i = 0
        while tickets[k] > 0:
            if tickets[i] > 0:
                ans +=1
                tickets[i] -=1
            i +=1
            if i == len(tickets):
                i = 0
        # print (ans)
        return ans