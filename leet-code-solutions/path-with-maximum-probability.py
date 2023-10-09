class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        cost = defaultdict(int)
        
        dic = defaultdict(list)
        
        i = 0
        for x, y in edges:
            cost[(x, y)] = succProb[i]
            cost[(y ,x)] = succProb[i]
            dic[x].append(y)
            dic[y].append(x)
            i += 1 
        
        check = defaultdict(int)
        vis = set()
        
        que = deque()
        que.append((start_node, 1))
        
        # vis.add()
        ans = 0
        
        # print(cost[(0,2)])
        while que:
            
            node, prob = que.popleft()
            
            # print(node, prob)
            
            if node == end_node:
                # print("yes")
                if ans < prob:
                   ans = prob
            for edge in dic[node]:
                    # print((edge, node, prob * cost[(edge, node)]))
                    if prob * cost[(edge, node)] > check[(edge, node)]:
                        
                        check[(node, edge)] = check[(edge, node)] = prob * cost[(edge, node)]
                        que.append((edge, prob * cost[(edge, node)]))
                        # vis.add((node, edge))
                        # vis.add((edge, node))
        return ans
                        
    