class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
       int size = pushed.length;
       Stack<Integer> stack = new Stack<>();
        
       int checker = 0, x = 0;
       while(x < size){
           stack.push(pushed[x]);
           while (!stack.isEmpty() && stack.peek() == popped[checker]){
               stack.pop();
               checker++;
           }
          x++; 
       }
        
    boolean ret = false; 
        
        if(checker == size)
            ret = true;
        
        return ret;
    }
}
