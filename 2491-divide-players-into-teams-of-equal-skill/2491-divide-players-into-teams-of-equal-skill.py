class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        size = len(skill)
        if sum(skill) % (size / 2) == 0:
            target = sum(skill) / (size / 2)
            skill.sort()
            left = 0
            right = size -1
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
            
        return int(ans)
        
        
        