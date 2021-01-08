class QuickSort{
    public static int partition(int[]arr,int l, int h){
        int i=l-1;
        int pivot=arr[h];
        for(int j=l;j<h;j++){
            if(arr[j]<pivot){
                i+=1;
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;

            }
        }
        int temp=arr[i+1];
        arr[i+1]=arr[h];
        arr[h]=temp;

        return i+1;

    }
    public static void quick(int[] arr,int l, int h){
        if(l<h){
            int pi=partition(arr,l,h);
            quick(arr,l,pi-1);
            quick(arr,pi+1,h);
        }
    }
    public static void print(int []arr){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        QuickSort qs=new QuickSort();
        int[] arr={10,15,5,20,7};
        qs.quick(arr,0,arr.length-1);
        qs.print(arr);
    }
}