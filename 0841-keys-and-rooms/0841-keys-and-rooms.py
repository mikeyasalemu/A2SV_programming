class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set()
        self.visited.add(0)
        self.bfs(rooms[0],rooms)
        return len(self.visited) == len(rooms)
    def bfs(self,room,rooms):
        childs = []
        
        size = len(room)
        
        for key in room:
            self.visited.add(key)
            for val in rooms[key]:
                if val not in self.visited:
                    childs.append(val)
        
        if childs:
            self.bfs(childs,rooms)
        