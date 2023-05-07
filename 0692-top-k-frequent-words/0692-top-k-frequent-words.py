class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        ans = []
        for key, val in dic.items():
            ans.append((-1*val,key))
        heapify(ans)
        ret = []
        for i in range(k):
            ret.append(heappop(ans)[-1])
        # print(ret)
        
        return ret
