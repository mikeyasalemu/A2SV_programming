class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) -1
        left = 0
        while right >= left:
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1