class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        unique = list(freq.keys())    
        n = len(unique)
        k = n-k 
        def quickSelect(l,r): 
            pivot = unique[r] 
            i = l 
            for j in range(l,r): 
                if freq[unique[j]]<=freq[pivot]: 
                    unique[i],unique[j]=unique[j],unique[i]
                    i+=1 
            unique[i],unique[r]=unique[r],unique[i] 
            if i>k: 
                return quickSelect(l,i-1)
            elif i<k: 
                return quickSelect(i+1,r)
            else:
                return unique[i]
        quickSelect(0,n-1)
        
        return unique[k:]