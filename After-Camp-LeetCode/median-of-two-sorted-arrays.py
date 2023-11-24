class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            # Split the array into two halves
            middle = len(arr) // 2
            left_half = arr[:middle]
            right_half = arr[middle:]

            # Recursively sort each half
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)

            # Merge the sorted halves
            return merge(left_half, right_half)

        def merge(left, right):
            merged = []
            left_index, right_index = 0, 0

            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            # Append any remaining elements
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])

            return merged

    # Example usage:
        arr = nums1 + nums2
        sorted_arr = merge_sort(arr)
        # print("Sorted array:", sorted_arr)
        ans = 0
        if len(sorted_arr) % 2 == 1:
            ans = sorted_arr[(len(sorted_arr)//2)]
        else:
            temp = sorted_arr[(len(sorted_arr)//2)] + sorted_arr[(len(sorted_arr)//2) -1]

            ans = temp / 2 
        # print(ans)

        return ans