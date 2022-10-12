class Solution {
    public int evalRPN(String[] tokens) {
         Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < tokens.length; i ++){
            int num1=0, num2=0;
            if(tokens[i].equals("+")){
                num2 =stack.pop();
                num1 =stack.pop();
                stack.push(num1 + num2);
            }
           else if(tokens[i].equals("*")){
                num2 =stack.pop();
                num1 =stack.pop();
                stack.push(num1 * num2);
            }
            else if(tokens[i].equals("/")){
                num2 =stack.pop();
                num1 =stack.pop();
                stack.push((int)Math.floor(num1 / num2));
            }
             else if(tokens[i].equals("-")){
                num2 = stack.pop();
                num1 = stack.pop();
                stack.push(num1 - num2);
            }
            else 
                stack.push(Integer.parseInt(tokens[i]));                     
      }
        
         return stack.pop();
  }
 }
 
