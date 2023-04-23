class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(set)
        for node1 , node2 in roads:
            dic[node1].add(node2)
            dic[node2].add(node1)
        # print(dic)
        ans = 0
        for i in range(n):
            for j in range(n):
                temp = 0
                if i == j:
                    continue
                else:
                    temp = len(dic[i]) + len(dic[j])
                    if i in dic[j]:
                        temp -=1
                    ans = max(temp, ans)
        return ans