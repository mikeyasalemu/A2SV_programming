class Solution {
    public int compress(char[] chars) {
        int  count = 1, size  = chars.length;
        if(chars.length == 1) return 1;
       int  j = 1, i = 0, temp = 0;
        
        while(j < chars.length){

            if (chars[i] == chars[j] ){
                count++;
            }
            
            else if(chars[i] != chars[j]){
           chars[temp++] = chars[i];
                
             if(count != 1){
                for(char c: Integer.toString(count).toCharArray()){
                    chars[temp++] = c;
                }
               }
                i = j;
                count = 1;   
               }
            
             if(j == chars.length - 1){
                  chars[temp++] = chars[i];
                 
                 if(count != 1){
                 
                for(char c: Integer.toString(count).toCharArray()){
                   
                    chars[temp++] = c;
                }
               }
            }
             j++;
        }
     return temp;  
       
    }
}

