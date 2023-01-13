class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
            arr = []
            for i in range(len(strs[0])):
                    arr.append("")
            for i in range(len(strs)):
                for j in range(len(strs[0])):
                    arr[j]+= strs[i][j]
            count = 0
            string1 = ""
            string1 = ""
            for i in range(len(arr)):
                string1 = "".join(sorted(arr[i]))
                string2 = arr[i]
                if string1 != string2:
                    count+=1
                
            return count