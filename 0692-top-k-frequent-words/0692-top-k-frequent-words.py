class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        ans = []
        n = len(words)
        for key, val in dic.items():
            ans.append((n - val,key))
        heapify(ans)
        ret = []
        for i in range(k):
            ret.append(heappop(ans)[-1])
        # print(ret)
        
        return ret
