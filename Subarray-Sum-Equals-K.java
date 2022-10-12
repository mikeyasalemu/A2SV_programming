class Solution {
    public int subarraySum(int[] nums, int k) {
        int sub = 0;
        for(int i = 0; i < nums.length; i++){
            int sumR = nums[i];
            
            if(nums[i] == k){
                sub++;
            }
            for (int z = i +1; z < nums.length; z++){
                 sumR = sumR + nums[z];
                 if(sumR == k){
                    sub++;
                }
            }
        }
        return sub;
    }
}
