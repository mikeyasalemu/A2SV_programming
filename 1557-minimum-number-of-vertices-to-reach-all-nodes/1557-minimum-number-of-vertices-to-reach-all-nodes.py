class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for node1 , node2 in edges:
            dic[node2].append(node1)
        print(dic)
        ans = []
        for lst in range(n):
            if len(dic[lst]) == 0:
                # print(dic[lst])
                ans.append(lst)
                           
        return ans
        