class Solution {
    public int longestSubarray(int[] nums) {
         int n = nums.length;
        int[] pref = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            pref[i] = pref[i - 1];
            if (nums[i - 1] == 0)
                pref[i]++;
        }
       int left = 0, ans = 0;
        int right = 0;
        while (right <= n) {
            while (pref[right] - pref[left] > 1)
                left++;
            ans = Math.max(ans, right - left - 1);
            right++;
        }
       return ans;
    }
}
