class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] less = new int[nums.length];
        int x;
        for (int i = 0; i < nums.length; i++)
        {
            x = 0;
            for(int j = 0; j < nums.length; j++)
            {
                if(nums[i] > nums[j])
                {
                    x++;
                }
            }
            less[i] = x;
        }
        return less;
    }
}
