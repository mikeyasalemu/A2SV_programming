class Solution {
    public List<String> fizzBuzz(int n) {
    List<String> num = new ArrayList<String>();
        for(int i=1; i<=n; i++){
            String s=String.valueOf(i);
            if (i % 3 == 0 && i % 5 == 0){
                num.add("FizzBuzz");
            }
            else if (i % 3 == 0){
                 num.add("Fizz");
            }
            else if (i % 5 == 0){
                 num.add("Buzz");
            }
            else{
                num.add(s);
            }
        }
        return num;
    }
}
