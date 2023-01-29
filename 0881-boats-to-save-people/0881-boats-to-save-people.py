class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size =  len(people)
        if size == 1:
            return 1
        ans =  0
        i = 0
        j = size -1
        while i <= j:
            if people[i] +  people[j] <= limit :
                i +=1
                
            ans +=1
            j -=1
               
        return ans
        