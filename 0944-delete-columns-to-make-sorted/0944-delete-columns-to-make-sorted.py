class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for chars in zip(*strs):
            # string = list(chars)
            # string2 = sorted(chars)
            if list(chars) != sorted(chars):
                count += 1
        return count
