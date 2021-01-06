import java.util.*;
import java.util.Scanner;
class Countsetbits{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        // System.out.print(Integer.toBinaryString(n));
        System.out.print(countSet(n));
    }
    public static int countSet(int n){
        int res=0;
        while(n>0){
            if(n%2!=0){
                res+=1;
            }
            n=n/2;
        }
        return res;
    }
}