class Solution {
    public boolean isValid(String s) {
        Stack<Character> check = new Stack<>();
         boolean ret = false;
           for(int i = 0; i < s.length(); i++){
            switch(s.charAt(i)){
                  case '{':
                      check.push('}');
                       break;
                  case '(':
                    check.push(')');
                    break;
                 case '[':
                    check.push(']');
                    break;
                default:
                    if(!check.isEmpty() && check.peek() == s.charAt(i) ){
                        check.pop();
                    }
                    else
                        return false;
                   
            }
        }
        return (check.isEmpty())? true: false;
 }
}
