class Solution {
    public int[] productExceptSelf(int[] nums) {
        int p[] = new int [nums.length];
        int pl[] = new int [nums.length];
        int pr[] = new int [nums.length];
         pl[0] = 1;
         pr[nums.length - 1] = 1;
        for(int i = 1; i < nums.length; i ++ ){
           pl[i] = pl[i - 1] * nums[i -1];
        }
        for(int j = nums.length - 2; j >= 0; j--){
            pr[j] = pr[j + 1] * nums[j + 1];
        }
         for(int k = 0; k < nums.length; k ++ ){
           p[k] = pl[k] *  pr[k];
        }
      return p;
}
}
