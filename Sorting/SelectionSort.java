class SelectionSort{
    public static void selsort(int[] arr){
        int n=arr.length;
        for(int i=0;i<n;i++){
            int min_idx=i;
            for(int j=i+1;j<n;j++){
                if(arr[min_idx]>arr[j]){
                    min_idx=j;
                }
            }
            int temp=arr[min_idx];
            arr[min_idx]=arr[i];
            arr[i]=temp;
        }
    }
    public static void print(int [] arr){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        SelectionSort sel=new SelectionSort();
        int [] arr={10,15,5,20,7};
        sel.selsort(arr);
        sel.print(arr);
    }
}