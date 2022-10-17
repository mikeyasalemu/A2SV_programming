class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length-1;
        int max = 0;
        while(left < nums.length/2){
            
          max = Math.max(max,nums[right] + nums[left]);   
            
            left++;
            right--;
        }
        return max;
    }
}
