import java.util.*;
class Node{
    int data;
    Node next;
    Node(int x){
        data=x;
        next=null;
    }
}

class ReverseSingleLL{
    public static Node reverseLL(Node head){
        ArrayList<Integer> al=new ArrayList<>();
        for(Node cur=head;cur!=null;cur=cur.next){
            al.add(cur.data);
        }
        for(Node cur=head;cur!=null;cur=cur.next){
            cur.data=al.remove(al.size()-1);
        }
        return head;
    }
    public static void printList(Node head){
        Node cur=head;
        while(cur!=null){
            System.out.print(cur.data+" ");
            cur=cur.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        head.next=new Node(20);
        head.next.next=new Node(30);
        head.next.next.next=new Node(40);
        reverseLL(head);
        printList(head);
    }
}