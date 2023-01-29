class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        if sum(skill) % (len(skill) / 2) == 0:
            target = sum(skill) / (len(skill) / 2)
            skill.sort()
            left = 0
            right = len(skill) -1
            while left < right:
                if skill[left] + skill[right] == target:
                    ans+= skill[left] * skill[right]
                    right -= 1
                    left += 1
                else:
                    ans = -1
                    break
        else:
            ans = -1
            
        return ans
        
        
        