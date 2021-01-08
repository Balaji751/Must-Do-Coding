class BubbleSort{
    public static void bubble(int[]arr){
        int n=arr.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
    public static void print(int[]arr){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        BubbleSort bs=new BubbleSort();
        int []arr={10,15,5,20,7};
        bs.bubble(arr);
        bs.print(arr);
    }
}