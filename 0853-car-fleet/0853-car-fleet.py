class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reach = []
        for i in range(len(position)):
            reach.append([position[i],speed[i]])
        reach.sort(reverse = True)
        stack = []
        for i in range(len(reach)):
            temp = (target - reach[i][0]) / reach[i][1]
            if stack and temp <= stack[-1]:
                continue 
            stack.append(temp)
        return len(stack)
        