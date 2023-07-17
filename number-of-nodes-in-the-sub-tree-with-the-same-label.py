class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        dic =defaultdict(list)
        for edge1, edge2 in edges:
            dic[edge1].append(edge2)
            dic[edge2].append(edge1)
            
        ans = [0]*len(labels)
        dic2 = defaultdict(int)
        vis = set()
        def dfs(par):
            
            previous = dic2[labels[par]]
            dic2[labels[par]] += 1
            vis.add(par)
            for node in dic[par]:
                if node not in vis:
                     dfs(node)
            
            ans[par] = dic2[labels[par]] - previous

            
        dfs(0)
        return ans