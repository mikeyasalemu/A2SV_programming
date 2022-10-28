class Solution {
    public int maxArea(int[] height) {
        
        int ret = 0, left = 0, right =  height.length - 1, holder = 0;
        while(left < right){
           
            if(height[right] < height[left]){
                holder = height[right] * (right - left);
                ret= Math.max(ret, holder);
                right --;
            }
            else{
                 holder = height[left] * (right - left);
                 ret= Math.max(ret, holder);
                left++;
            }
        }
        return ret;
    }
}
