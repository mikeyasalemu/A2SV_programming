class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer1= 0
        pointer2 =1
        count = 1
        ch = chars[0]
        if len(chars) ==1:
            return 1
        while pointer2 < len(chars):
            if chars[pointer2] != ch:
                chars[pointer1] = ch
                pointer1 +=1
                temp =  list(str(count))
                if count > 1:
                    for i in temp:
                        chars[pointer1] = str(i)
                        pointer1 +=1
                count = 1
                ch = chars[pointer2]
            else:
                count +=1
            pointer2 +=1            
            if pointer2 == len(chars):
                chars[pointer1] = ch
                pointer1 +=1
                temp =  list(str(count))
                if count > 1:
                    for i in temp:
                        chars[pointer1] = str(i)
                        pointer1 +=1
                
        return pointer1