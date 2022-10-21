class Solution {
    public String reverseParentheses(String s) {
        Stack<String> stack = new Stack<>();
        String holder = "";

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ')')
                stack.push(Character.toString(s.charAt(i)));
            else {
                holder = "";
                if (!stack.empty())
                    while (!stack.peek().trim().equals("(")) {
                        holder += stack.pop();
                        if (stack.empty())
                            break;
                    }

                if (!stack.empty())
                    stack.pop();
                for (int j = 0; j < holder.length(); j++) {
                    stack.push(Character.toString(holder.charAt(j)));
                }
            }
        }
       String ret = "";
        for (int i = 0; i < stack.size(); i++) {
            ret+=stack.get(i);
        }

        return ret;
    }
}
