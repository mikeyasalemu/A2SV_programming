class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        index2 = 0
        size = len(nums1)
        dif = m
#         iterate until the size of nums1
        while index < size:
            if index2 == n:
                break
                
#           compare values from both list to put at the exact place
            elif nums2[index2] < nums1[index]:
                nums1.insert(index, nums2[index2])
                index2+=1
                dif +=1
                nums1.pop()
                
#           if the numbers remaining in mums2 are all grater than nums1..
            elif index >= dif:
                nums1[index] = nums2[index2]
                index2+=1
                dif +=1

            index +=1
                