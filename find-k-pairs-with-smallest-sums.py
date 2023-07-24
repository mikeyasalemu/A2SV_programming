class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        result = []

        for i in range(len(nums1)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and min_heap:
            _, i, j = heappop(min_heap)  
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                
                heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

            k -= 1

        return result