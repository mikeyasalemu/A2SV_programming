class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] > nums2[j]:
                j +=1
            elif nums1[i] < nums2[j]:
                 i += 1
            elif nums1[i] == nums2[j] and nums1[i] not in ans:
                ans.add(nums1[i])
            else:
                i+=1
                j+=1
            
        return list(ans)