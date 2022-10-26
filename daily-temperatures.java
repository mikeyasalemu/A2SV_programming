class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack=new Stack();
        int[] ret=new int[temperatures.length];
        
        int index = 0;
        for(int i=0; i<temperatures.length; i++){
            
            while(!stack.isEmpty() && temperatures[stack.peek()]< temperatures[i]){
                index = stack.pop();
               
                ret[index] = i - index;
               
            }
            stack.push(i);
        }
        
      
        return ret;
    }
}
