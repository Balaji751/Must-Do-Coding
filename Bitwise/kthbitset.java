import java.util.*;
import java.util.Scanner;
class kthbitset{
    public static void kthBitset(int n,int k) {
        if(Integer.toBinaryString(n) &(1<<(k-1))!=0){
            System.out.print("Yes");
        }
        else{
            System.out.print("No");
        }
    }
    public static void main(String[] args) {
        // Scanner sc=new Scanner(System.in);
        int n=5;
        int k=3;
        kthBitset(n,k);
    }
}