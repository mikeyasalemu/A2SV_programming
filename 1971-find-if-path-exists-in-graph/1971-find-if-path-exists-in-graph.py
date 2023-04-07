class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.destinition = destination
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        return self.dfs(source,visited,graph)
    def dfs(self,node,visited,graph):
        if node == self.destinition:
            return True
        
        visited.add(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                found = self.dfs(neighbour,visited,graph)
                if found:
                    return True
        return False