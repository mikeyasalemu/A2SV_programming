class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        dic = defaultdict(int)
        self.max = [persons[0]]
        dic[persons[0]] +=1
        for i in range(1,len(persons)):
            dic[persons[i]]+=1
            if dic[self.max[-1]] > dic[persons[i]]:
                self.max.append(self.max[-1])
            else:
                 self.max.append(persons[i])
        # print(self.max)
        self.times = times
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) -1
        while left <= right:
            mid = left + (right - left)// 2
            
            if self.times[mid] > t:
                right = mid -1
            else:
                left = mid+1
        # print(left)
        return self.max[left-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)