import java.util.*;
class PowerofTwo{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.print(ispow2(n));
    }
    public static boolean ispow2(int n){
        if(n==0) return false;
        while(n!=1){
            if(n%2!=0) return false;
            n=n/2;
        }
        return true;
    }
}