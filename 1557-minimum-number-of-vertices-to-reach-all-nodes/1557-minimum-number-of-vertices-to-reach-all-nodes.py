class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for node1 , node2 in edges:
            dic[node2].append(node1)
        ans = []
        for lst in range(n):
            if len(dic[lst]) == 0:
                ans.append(lst)
                           
        return ans
        