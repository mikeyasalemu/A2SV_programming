class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        index2 = 0
        size = len(nums1)
        dif = m
        # print (dif)
        while index < size:
            if index2 == n:
                break
            elif nums2[index2] < nums1[index]:
                nums1.insert(index -1, nums2[index2])
                # index+=1
                index2+=1
                dif +=1
                nums1.pop()
            elif index >= dif:
                # nums1.insert(index -1, nums2[index2])
                nums1[index] = nums2[index2]
                index2+=1
                dif +=1

            index +=1
                