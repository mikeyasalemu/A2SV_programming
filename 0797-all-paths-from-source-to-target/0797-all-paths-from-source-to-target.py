class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for index, val in enumerate(graph):
            dic[index] = val
        target = len(graph) -1
        visited = set()
        ans = []
        def dfs(node,arr):
            arr.append(node)
            if node == target:
                ans.append(arr)
                visited.discard(node)
                return
            visited.add(node)
            for edge in dic[node]:
                if edge not in visited:
                    dfs(edge,arr[:])
            visited.discard(node)
            return
        
        dfs(0,[])
        # print(ans)
        return ans