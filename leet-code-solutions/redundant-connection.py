class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1

        def connected( x, y):
            return find(x) == find(y)

        ans = []
        for x,y in edges:
            
            if connected(x,y):
                ans.append([x,y])
            else:
                union(x,y)
        

        return ans[-1]