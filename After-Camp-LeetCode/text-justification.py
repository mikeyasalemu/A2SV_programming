class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        
        def simulate(curr, space, ind):
            
            gap = 1
            if len(curr) > 1:
                gap = len(curr) -1
            
            _space = space // gap
            add_space = space % gap
            
            # print(_space, add_space)
            string = ""
            sp = [" "] * _space
            
            sp = "".join(sp)
            
            if (gap == 1 and len(curr) == 1 )or ind == len(words) -1:
                
                
                for i in range(len(curr)):
                    if space > 0:
                         string += words[curr[i]] + " "
                         space-=1
                    else:
                        string += words[curr[i]]
                            
                sp = [" "] * (space)
                sp = "".join(sp)
                
                string += sp
            else:
                for i in range(len(curr)):

                    string+= words[curr[i]]

                    if gap > 0:

                        string+= sp
                        gap -=1

                    if add_space > 0:

                        string+= " "
                        add_space -=1
            
            return string
 
        
        width = 0
        curr = []
        
        
        for i in range(len(words)):

            width += len(words[i])+1
            curr.append(i)
            
            if (i+1 < len(words) and (width + len(words[i+1])) > maxWidth) or i+1 == len(words):
                temp = maxWidth - (width - len(curr))
                # print(width, temp)
                ans.append(simulate(curr, temp, i))
                
                width = 0
                curr =[]
        
        # print(ans)
        
        return ans
            
            
                    