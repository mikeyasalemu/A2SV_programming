class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapify(nums)
        ans = []
        ans.append(set())
        dic = defaultdict(lambda: 1001)
        while nums:
            temp = heappop(nums)
            check = False
            
            for  i in range(len(ans)-1,-1,-1):
                if dic[i] != 1001 and  temp - dic[i] > 1:
                    break
                if temp not in ans[i] and (len(ans[i]) == 0 or temp -dic[i] == 1):
                    ans[i].add(temp)
                    dic[i] = temp
                    check = True
                    break
                    
            if not check:
                ans.append(set())
                ans[-1].add(temp)
                dic[len(ans)-1] = temp
                
        # print(ans,len(ans))  
        for i in range(len(ans)):
            if len(ans[i]) < 3:
                return False
        return True