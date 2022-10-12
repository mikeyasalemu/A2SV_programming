class MyQueue {

    Stack<Integer> myQueue;
    public MyQueue() {
        myQueue = new Stack<>();
    }
    
    public void push(int x) { 
       myQueue.push(x);
        
    }
    
    public int pop() {
       return  myQueue.remove(0);
    }
    
    public int peek() {
      return myQueue.firstElement();
    }
    
    public boolean empty() {
       return myQueue.empty(); 
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
