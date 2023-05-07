class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        ans = []
        for key, val in dic.items():
            ans.append((val,key))
        dic2 = defaultdict(list)
        for key,val in dic.items():
            dic2[val].append(key)
        dic = OrderedDict(sorted(dic2.items(), reverse=True, key=lambda t: t[0]))
        ans  =[]
        for key,val in dic.items():
            heapify(val)
            while val and k > 0:
                ans.append(heappop(val))
                k-=1
            if k == 0:
                break
        # print(ans)
        return ans
#         heapify(ans)
#         ret = nlargest(k,ans)
#         heapify(ret)
#         ans = []
#         dic = defaultdict(list)
        
#         while ret:
#             freq , key = heappop(ret)
#             dic[freq].append(key)
            
#         dic = OrderedDict(sorted(dic.items(), reverse=True, key=lambda t: t[0]))
        
#         for key,val in dic.items():
#             heapify(val)
#             while val:
#                 ans.append(heappop(val))
        # print(ans)
        # # print(nlargest(k,ans,key = lambda x:(x[0],x[1])))
        # return ans