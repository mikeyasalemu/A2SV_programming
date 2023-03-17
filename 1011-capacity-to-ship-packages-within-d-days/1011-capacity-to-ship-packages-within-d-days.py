class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # print(list(accumulate(weights)))
        right = sum(weights)
        left = 1
        # print(3%2)
        while left < right:
            mid =(left+right)//2
            ans = 1
            pre_sum = 0
            for i in range(len(weights)):
                if pre_sum + weights[i] > mid:
                    if weights[i] > mid:
                        ans+= weights[i]//mid
                        if weights[i] % mid != 0:
                            ans+=1
                        pre_sum = 0
                    else:
                        ans+=1
                        pre_sum = weights[i]
                else:
                    pre_sum+= weights[i]
            # print(mid,ans)
            if ans > days or mid < max(weights):
                left = mid+1
            elif ans <= days:
                right = mid
            
        
        return left