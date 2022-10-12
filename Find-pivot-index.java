class Solution {
    public int pivotIndex(int[] nums) {
        
        int size = nums.length;
        for(int i = 0; i < size; i++){
            int sumL = 0,sumR = 0 ;
           for(int j = 0; j < i; j++) {
               sumL = sumL + nums[j];
               
           }
            
           for(int k = i + 1; k < size; k++) {
               sumR = sumR + nums[k];
               
           }
            if(sumR == sumL){
                return i;
            }
        }
        return -1;
    }
}
