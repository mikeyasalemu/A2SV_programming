 class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n = nums.length;
        int sum = 0;
        int[] arr = new int[n+1];
        Arrays.fill(arr, 0);
        arr[0] = 1;
        int ans = 0;
/*
   it updates the arr on the sum position and itrates in it when sum is not 
   updated. arr's 'index' or key is Sum
 


*/
        for(int i = 0; i < n; i++){
            if (nums[i] % 2 == 1)
                sum++;
            if (sum >= k){
                ans += arr[sum - k];
            }
            arr[sum] += 1;
        }
        return ans;
    }
}
    
