class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        ans = [-1]*len(intervals)
        for i in range(len(intervals)):
            temp = intervals[i][1]
            left = i
            right = len(intervals) -1
            while left <= right:
                mid = left + (right-left)//2
                if intervals[mid][0] >= temp:
                    right = mid-1
                else:
                    left = mid +1
                  
            if left <= len(intervals)-1:
                ans[intervals[i][2]] = intervals[left][2]
        return ans