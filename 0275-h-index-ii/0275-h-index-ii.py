class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        check = False
        while left <= right:
            mid =(left+right)//2
            if (len(citations) - mid) <= citations[mid]:
                right = mid -1
                check = True
            else:
                left = mid+1
        if check:
            return len(citations) - left
        return 0