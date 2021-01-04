class Node{
    int data;
    Node prev;
    Node next;

    Node(int x){
        data=x;
        next=prev=null;
    }
}

class DoublyLL{
    public static void printList(Node head){
        Node cur=head;
        while(cur!=null){
            System.out.print(cur.data+" ");
            cur=cur.next;
        }
    }
    public static void main(String[] args) {
        Node head=new Node(10);
        Node t1=new Node(20);
        Node t2=new Node(30);
        head.next=t1;
        t1.next=t2;
        t2.next=null;
        t2.prev=t1;
        t1.prev=head;
        printList(head);
    }
}