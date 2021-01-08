class InsertionSort{
    public static void insert(int[]arr){
        int n=arr.length;
        for(int i=1;i<n;i++){
            int key=arr[i];
            int j=i-1;
            while(j>=0 && arr[j]>key){
                arr[j+1]=arr[j];
                j-=1;
            }
            arr[j+1]=key;
        }
    }
    public void toString(int[]arr){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        InsertionSort in=new InsertionSort();
        int[] arr={10,15,5,20,7};
        // int n=arr.length;
        in.insert(arr);
        in.toString(arr);
    }
}