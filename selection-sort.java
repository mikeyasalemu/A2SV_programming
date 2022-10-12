

class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        // System.out.println(i + arr.toString());
         int min_index = i;
        
        for(int j = i+1; j < arr.length; j++){
            
            if(arr[min_index] > arr[j]){
                min_index = j;
            }
        }
        
           int temp = arr[i];
           arr[i] = arr[min_index];
           arr[min_index] = temp;
           return 0;
	}
	
	void selectionSort(int arr[], int n)
	{
	    
	    //code here
	     for( int i = 0; i < n-1; i++)
	    {
        select(arr,i);
        }
	}
}
