class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if len(people) == 1:
            return 1
        ans =  0
        i = 0
        j = len(people) -1
        while i <= j:
            if people[i] +  people[j] <= limit :
                i +=1
                
            ans +=1
            j -=1
               
        return ans
        