class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
    int n = nums.length;
    int max = 0, sum1 = 0, sum2 = 0, size1 = firstLen, size2 = secondLen, Flag = 0;
    if(firstLen < secondLen){
        size1 = secondLen;
        size2= firstLen;
    }
    int i = 0;
    int right = 0 , left = 0;
    while ( i < n){ 
        if(i == 0){
            for(int j = 0; j < size1; j++){
          sum1 += nums[j];
             }
            i = size1;
           
        }
        else if(i > 0){
             sum1 +=nums[i] - nums[i-size1]; 
            i++;
             
        }
        
        //////////////////
        left = 0;
        sum2 = 0;
        Flag = 0;
         if(i - size1 +1 > size2 ){
         while(left <  i - size1 ){
             
             if(Flag == 0){
                 
            for(int j = left; j < left+size2; j++){
          sum2 += nums[j];
             }
            left = size2 ;
         }
        else if(Flag > 0){
             sum2 +=nums[left] - nums[left-size2];
            left++;
        }
         
              max = Math.max(max, sum1 + sum2);  
           
             Flag = 1;
         }
        }
        //////////////////
        right = i;
        sum2 = 0;
        if( i + size2 < n){
            
        while(right < n){
            
            if(right == i ){
                 
            for(int j = right; j < right+size2; j++){
                  sum2 += nums[j];
                   }
                  right += size2;
            }
        else if(right > i){
                sum2 +=nums[right] - nums[right-size2]; 
                  right++;
              }
             
           max = Math.max(max, sum1 + sum2);  
           
         }  
        
      }
    }  
        return max;
    }
}
