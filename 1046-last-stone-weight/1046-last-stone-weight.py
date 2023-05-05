class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(stones)
       
        while len(list(stones)) > 1:
            x,y = nlargest(2,stones)
            stones.remove(x)
            stones.remove(y)
            if x == y:
                heapify(stones)
                continue
            else:
                heapify(stones)
                heappush(stones,x-y)
        stones = list(stones)
        if stones:
            return stones[0]
        return 0