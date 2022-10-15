class Solution {
    public int[] rearrangeArray(int[] nums) {
        int temp = 0;
        for(int i = 1; i < nums.length - 1;i++){           
           if((nums[i-1] + nums[i+1]) / 2 == nums[i]){
                temp = nums[i] ;
               nums[i] = nums[i + 1];
               nums[i + 1] =temp;
             if (i >= 2){
                i -= 2 ; 
             }
               else i--;
           }   
          
        }
       return nums; 
    }
}
