class Solution {
    public void rotate(int[] nums, int k) {
       int[] arr = new int[nums.length];
         Arrays.fill(arr, 0);
        for(int l = 0; l < nums.length; l++){
            arr[l] = nums[l];
        }
         Arrays.fill(nums, 0);
      int i = 0, j = nums.length - 1 , z = 0;
        while(i < nums.length){
            if(k > nums.length){
                k = k % nums.length;
            }
             if(k > 0){
               nums[k - 1] = arr[j];
                j--;
                k--;
                i++;
            }
            else if(k == 0){
               nums[i] = arr[z];
                i++;
                z++;
            } 
           
            
        }
    }
}
