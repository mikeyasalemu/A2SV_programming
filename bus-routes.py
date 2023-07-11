class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(set)

        for i, route in enumerate(routes):
            for node in route:
                dic[node].add(i)
        
        ans = -1
        visited = set()
        queue = deque()
        queue.append(source)

        while queue:
            size = len(queue)
            ans+= 1

            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return ans
                
                for bus in dic[curr]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.extend(routes[bus])
        return -1